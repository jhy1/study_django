import time
from queue import Queue
from threading import Thread

q = Queue()


def set_num():
    for i in range(200):
        q.put(i)
    # print(type(q.qsize()))
    print("我在生产")


def put_num():
    for i in range(20):
        q.get()
    if q.qsize() < 10:
        time.sleep(2)
    print("我在消费")


def main():
    while True:
        if q.qsize() < 50:
            time.sleep(1)
            set_num()
        if q.qsize() > 20:
            put_num()


if __name__ == '__main__':
    # main()
    t1 = Thread(target=main)
    t1.start()
