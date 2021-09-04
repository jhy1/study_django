#1   python的线程无法利用多核CPU，在同一时间内，只能有一个线程在执行


#2
import time
from threading import Thread


class Mythread(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        print(self.url)

    def run(self):
        for i in range(len(self.url)):
            time.sleep(0.1)
            print("线程名字：{0}，这是数字{1}".format(self.name, self.url[i]))


if __name__ == '__main__':
    url = "baidu.com"
    name1 = ['baidu.com' for i in range(100)]
    # print(name1)
    t111 = time.time()
    print(t111)
    for i in range(4):
        t1 = Mythread(name1)
        t1.start()
    t1.join()
    t222 = time.time()
    # print(t222)
    print(t222-t111)
