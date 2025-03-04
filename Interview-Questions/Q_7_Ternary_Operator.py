'''
# Q.7. Explain the ternary operator in Python.

Unlike C++, we don’t have ?: in Python, but we have this: 
[on true] if [expression] else [on false]
If the expression is True, the statement under [on true] is executed. 
Else, that under [on false] is executed.

# Below is how you would use it:
    a, b = 2, 3
    min = a if a < b else b
    print(min)

Above will print 2.

# Run this cell to see the result.
    a, b = 10, 12
    print("Hi") if a < b else print("Bye")
    Hi

'''




