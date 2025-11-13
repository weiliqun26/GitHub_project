# ----------- 观察者接口 -----------
class Observer:
    """观察者（粉丝）的抽象基类"""

    def update(self, subject, message):
        """当收到通知时，此方法被调用"""
        raise NotImplementedError("子类必须实现此方法")


# ----------- 主题接口 -----------
class Subject:
    """主题（博主）的抽象基类"""

    def __init__(self):
        self._observers = []  # 用来保存观察者的列表

    def register(self, observer: Observer):
        """注册（关注）一个观察者"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"--- 系统消息: {observer.name} 关注了你 ---")

    def unregister(self, observer: Observer):
        """移除（取关）一个观察者"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"--- 系统消息: {observer.name} 取消关注了 ---")

    def notify(self, message):
        """通知所有已注册的观察者"""
        print("\n--- 博主发布了新动态，开始通知所有粉丝 ---")
        for observer in self._observers:
            observer.update(self, message)


# ----------- 具体的实现类 -----------
class Blogger(Subject):
    """具体的博主类"""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def publish_post(self, content):
        """发布新文章，并通知所有粉丝"""
        print(f"\n{self.name} 发布了新文章: '{content}'")
        self.notify(content)  # 调用父类的通知方法


class Fan(Observer):
    """具体的粉丝类"""

    def __init__(self, name):
        self.name = name

    def update(self, subject: Blogger, message):
        """实现更新方法，定义收到通知后的行为"""
        print(
            f"你好 {self.name}！你关注的博主 [{subject.name}] 发布了新内容: '{message}'"
        )


# ----------- 演示程序 -----------
if __name__ == "__main__":
    # 1. 创建一个博主（主题）
    blogger_geek = Blogger("技术极客")

    # 2. 创建几个粉丝（观察者）
    fan_a = Fan("小明")
    fan_b = Fan("小红")
    fan_c = Fan("小王")

    # 3. 粉丝关注博主
    blogger_geek.register(fan_a)
    blogger_geek.register(fan_b)

    # 4. 博主发布第一篇文章
    blogger_geek.publish_post("观察者模式原来这么简单！")

    # 5. 小红不想关注了
    blogger_geek.unregister(fan_b)

    # 6. 又有一个新粉丝小王
    blogger_geek.register(fan_c)

    # 7. 博主发布第二篇文章
    blogger_geek.publish_post("设计模式的魅力")
