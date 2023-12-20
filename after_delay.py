import time

def after_n_seconds(f, n):
    time.sleep(n)
    f()


def hello():
    print('Hello after delay!')

after_n_seconds(hello, 5)
after_n_seconds(hello, 2)
