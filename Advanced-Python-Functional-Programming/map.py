# map(iterable_parameter_function, list)

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1, 2, 3])))

# ---------------------------------------------
print("---------------------------------------------")
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list)
