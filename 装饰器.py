def login(func):
    def wrapper():
        func()
    return wrapper
@login
def data():
    print('11111')

data()