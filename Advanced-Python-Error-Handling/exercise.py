# Let's try first example. 
while True:
    try:
        age = int(input("What's your age: "))
        print(f'Your age is : {age}')
        10/age 
        raise ValueError("Hey, Cut it Out")
    except Exception as error:
        print(error)
    else:
        print("Thank you..!")
        break
    finally:
        print("OK.Bro.")

    print("Can you hear me ?")
