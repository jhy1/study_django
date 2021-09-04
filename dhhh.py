def login(func):
    def wrapper(a, b):
        try:
            num = func(a, b)
            return num
        except:
            print("不能为零")

    return wrapper


def quit(func):
    def wrapper(a, b):
        error_count = 0
        try:
            num = func(a, b)
            # return num
            # if num != False:
            #     print(11111111111111111111111111111)
            # print(222222222222222222)
        except:
            print(error_count)
            # if error_count < 3:
            #     func(a, b)
            #     print('jjjjjjjjjjjjjj')
            # error_count += 1
            while True:
                if error_count < 3:
                    # print(error_count)
                    print(1111111111)
                    func(a, b)
                    error_count += 1
                else:
                    break
                # error_count += 1

    return wrapper


# @login
# @quit
def work(a, b):
    res = a / b
    print('a除B的结果为:', res)


@quit
def work2(a, b):
    assert( a == b)

    # print('a除B的结果为:', res)


if __name__ == '__main__':
    # work(1, 0)
    print(work2(1, 11))