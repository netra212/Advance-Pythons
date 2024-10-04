# zip() : Pure function. 
# Two iterable can be zipped together or zipped the item together.

my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

print(list(zip(my_list, your_list, their_list)))

# zip iterates through each of them & zipped together.