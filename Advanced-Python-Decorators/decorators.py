# Higher Order function (HOC).
# HOC : Either accept the another function as parameter or return the function.
# Example: map(), reduce(), filter() are higher order function. 
# Decorator: Helps to add the extra functionality to the original function.

# Decorator Pattern.
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("****************")
        func(args, **kwargs)
        print("****************")
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

@my_decorator
def bye():
    print("See you later....")

# print(hello())
# print(bye())

# a = my_decorator(hello)
# print(a())

# b = my_decorator(bye)
# print(b())

hello('hiiii')


'''
# Practical Application of the Decorators:
-> 
'''