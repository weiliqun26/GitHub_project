from collections import defaultdict


class NewsAgency:
    """
    新闻通讯社 (事件中心/Broker)，负责处理话题的发布与订阅。
    """

    def __init__(self):
        # 使用defaultdict可以简化代码，当访问一个不存在的key时，会自动创建一个空列表
        self.subscribers = defaultdict(list)
        print("--- 新闻通讯社已开始运作 ---")

    def subscribe(self, topic, subscriber):
        """订阅一个新闻主题"""
        if subscriber not in self.subscribers[topic]:
            self.subscribers[topic].append(subscriber)
            print(f"--- (通讯社) '{subscriber.name}' 订阅了 '{topic}' 主题。---")

    def unsubscribe(self, topic, subscriber):
        """取消订阅一个新闻主题"""
        if subscriber in self.subscribers[topic]:
            self.subscribers[topic].remove(subscriber)
            print(f"--- (通讯社) '{subscriber.name}' 取消订阅 '{topic}' 主题。---")

    def publish(self, publisher_name, topic, article_title):
        """发布新闻到特定主题"""
        print(
            f"\n--- (通讯社) 收到来自 '{publisher_name}' 的一篇关于 '{topic}' 的新文章: '{article_title}' ---"
        )
        if topic in self.subscribers and self.subscribers[topic]:
            # 获取该主题的所有订阅者
            for subscriber in self.subscribers[topic]:
                # 调用订阅者的接收方法
                subscriber.receive_news(topic, article_title)
        else:
            print(f"--- (通讯社) 但目前无人订阅 '{topic}' 主题。---")


class NewsReader:
    """新闻读者 (订阅者)"""

    def __init__(self, name):
        self.name = name

    def receive_news(self, topic, article_title):
        """接收新闻的回调方法"""
        print(
            f"  -> [读者 {self.name}] 收到推送 - 主题: '{topic}', 标题: '{article_title}'"
        )


class Reporter:
    """记者 (发布者)"""

    def __init__(self, name, agency: NewsAgency):
        self.name = name
        self.agency = agency

    def write_article(self, topic, title):
        """撰写并发布文章"""
        print(f"[{self.name}]: 我刚写完一篇关于 '{topic}' 的文章，准备发布！")
        self.agency.publish(self.name, topic, title)


# ====================
# 演示程序
# ====================
if __name__ == "__main__":
    # 1. 创建一个新闻通讯社
    agency = NewsAgency()

    # 2. 创建几个读者 (订阅者)
    reader_tom = NewsReader("Tom")
    reader_jerry = NewsReader("Jerry")
    reader_sam = NewsReader("Sam")

    # 3. 读者订阅感兴趣的主题
    agency.subscribe("体育", reader_tom)
    agency.subscribe("体育", reader_jerry)
    agency.subscribe("科技", reader_jerry)
    agency.subscribe("科技", reader_sam)

    # 4. 创建记者 (发布者)
    reporter_sports = Reporter("体育记者-约翰", agency)
    reporter_tech = Reporter("科技记者-艾米", agency)

    # 5. 体育记者发布新闻
    # 预期: Tom和Jerry会收到
    reporter_sports.write_article("体育", "昨晚的决赛中，A队以3:2险胜B队！")

    # 6. 科技记者发布新闻
    # 预期: Jerry和Sam会收到
    reporter_tech.write_article("科技", "新型量子计算机取得重大突破")

    # 7. Jerry不再关心体育了
    agency.unsubscribe("体育", reader_jerry)

    # 8. 体育记者再次发布新闻
    # 预期: 只有Tom会收到
    reporter_sports.write_article("体育", "C选手刷新了世界纪录！")
