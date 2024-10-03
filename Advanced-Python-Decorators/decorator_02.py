# Decorator
from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        time1 = time()
        result = fn(*args, **kawrgs)
        time2 = time()
        total_time = time2 - time1
        print(f"time taken: {total_time} s")
        return result
    return wrapper

@performance 
def long_time():
    for i in range(100000):
        i*5

long_time()