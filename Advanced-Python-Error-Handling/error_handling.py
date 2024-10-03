# Error Handling. 

# Let's try first example. 
while True:
    try:
        age = int(input("What's your age: "))
        print(f'Your age is : {age}')
    except Exception as error:
        print(error)
    else:
        print("Thank you..!")
        break
    finally:
        print("OK.Bro.")

    print("Can you hear me ?")

# Let's try another example. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as error:
        print(error)
    else:
        print("Thank you....!")
    finally:
        print("OK..., I am finally done.")

print(sum(num1, num2))