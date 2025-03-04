# Q6: Write a program in Python to delete the first element from a list.

def deleteHeadFromList(list):
    del list[0]


a = [1, 2, 3]
print(a)
deleteHeadFromList(a)
print(a)
