# Generators specifical types of things in python which pause and resume functions. 
# list(range(100)) -> List creates a 100 items in memory but generator helps to increase value by 1. 

# range() -> is a kind of generator. 

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

