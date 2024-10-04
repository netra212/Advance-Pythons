# Functional Programming: Separation of concerns:
# Clear + Understandable.
# Easy to maintain.

# Pillars in the Functional Programming. 
    # -> Pure functions
    # There is the separation of the data of the program and functionality of the program.

# What is a pure function. ?
    # 1. -> Given the same input, it will always return the same output. 
    # 2. -> Function should not produce any side effects.

# Question1: Is this a Pure function ?
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

# Yes, Point 1 Pass. 
# Yes, Point 2 Pass, Because it does not effect outside world. Everything matter is inside the function.

# But if I change like this.
# Question2: Is this a pure function ?
new_list = []
def multiply_by3(li):
    for item in li:
        new_list.append(item*2)
    return print(new_list)

print(multiply_by3[1,2,3])

# No, this is not the pure function because it's interacting with the outside world, in this case, new_list. so, it has a side effects. 
# Also, function is returning the print something, It effects so. 