# In Python, we can create our own Objects in Python.
# Camel case is used while creating a class in Python. 

# Blue-print -> Class.
# Instance -> Object.
class BigObjects:
    def __init__(self) -> None:
        print("I am a Class.....!")

big_object = BigObjects()
print(big_object)

# ------ ------ ------ ------ ------ ------ ------
# Understanding the `class` and `Objects`.
# ------ ------ ------ ------ ------ ------ ------

def player_details():
    try:
        player_name = input("Enter player name: ")
        player_age = int(input("Enter player age: "))
    except Exception as error:
        print(error)
    else:
        print("OK.")

    return player_name, player_age

player_name, player_age = player_details()

print(f"Player name:  {player_name}")
print(f"player_age:  {player_age}")

class PlayerCharacter:
    '''Constructor: Automatically called while instantiating Objects.'''
    # This is called `dunder` method.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Run.OK")

player_character = PlayerCharacter(player_name, player_age)
print(f"Name of the player is : {player_character.name}")
print(f"Age of the player is : {player_character.age}")
print(player_character.run())




