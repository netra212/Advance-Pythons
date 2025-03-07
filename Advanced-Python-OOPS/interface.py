# Interface: Only define input and output of the thing but they don't specifiy the things. 
# Abstract class: Define the input and output of the things, but they also provide an implementations. 
# Generally, Interface and Abstract class cannot be instantiates on their own or are not able to create their own object. 

class Duck:
    def quack(self):
        print("Duck Quacks")

class Cat:
    def meow(self):
        print("Cat meows")

counter = 0

def make_it_quack(duck):
    global counter

    if counter > 0:
        duck.quack()
    else:
        counter += 1

if __name__ == "__main__":
    cat = Cat()
    cat.meow()
    make_it_quack(cat)

    print(dir(cat))