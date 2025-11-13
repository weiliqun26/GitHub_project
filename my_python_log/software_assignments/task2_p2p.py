class ChatServer:
    """
    聊天服务器，负责管理用户和消息的点对点路由。
    """

    def __init__(self):
        self.users = {}  # 存储在线用户，格式为 {username: user_object}
        print("--- 聊天服务器已启动 ---")

    def register(self, user):
        """用户登录注册"""
        if user.username not in self.users:
            self.users[user.username] = user
            print(f"--- (服务器) 用户 '{user.username}' 已上线。 ---")
        else:
            print(f"--- (服务器) 用户名 '{user.username}' 已被占用。 ---")

    def send_private_message(self, sender_username, receiver_username, message):
        """发送私聊消息"""
        print(
            f"--- (服务器) 收到 '{sender_username}' 发给 '{receiver_username}' 的消息。---"
        )
        receiver = self.users.get(receiver_username)
        if receiver:
            # 找到接收者，并调用其接收消息的方法
            receiver.receive_message(sender_username, message)
            print(f"--- (服务器) 消息已成功转发给 '{receiver_username}'。---")
        else:
            # 如果接收者不存在或不在线，通知发送者
            sender = self.users.get(sender_username)
            if sender:
                sender.receive_message(
                    "系统", f"发送失败，用户 '{receiver_username}' 不在线。"
                )
            print(f"--- (服务器) 错误：用户 '{receiver_username}' 不存在或不在线。 ---")


class ChatUser:
    """聊天用户，可以发送和接收消息"""

    def __init__(self, username, server: ChatServer):
        self.username = username
        self.server = server
        self.server.register(self)  # 用户实例化时自动在服务器注册

    def send_to(self, receiver_username, message):
        """向指定用户发送消息"""
        print(f"\n[{self.username} -> {receiver_username}]: {message}")
        self.server.send_private_message(self.username, receiver_username, message)

    def receive_message(self, sender_username, message):
        """接收消息的回调方法"""
        print(
            f"  -> [{self.username} 的聊天窗口] 收到来自 <{sender_username}> 的消息: {message}"
        )


# ====================
# 演示程序
# ====================
if __name__ == "__main__":
    # 1. 实例化一个服务器
    server = ChatServer()

    # 2. 创建几个用户 (他们会自动在服务器注册)
    user_alice = ChatUser("Alice", server)
    user_bob = ChatUser("Bob", server)
    user_charlie = ChatUser("Charlie", server)

    # 3. Alice给Bob发消息
    # 预期: 只有Bob会收到
    user_alice.send_to("Bob", "嗨，Bob，下午有空吗？")

    # 4. Charlie给Alice发消息
    # 预期: 只有Alice会收到，Bob不受影响
    user_charlie.send_to("Alice", "你的报告写完了吗？")

    # 5. Bob尝试给一个不存在的用户David发消息
    # 预期: 服务器会通知Bob发送失败
    user_bob.send_to("David", "你好，David！")
