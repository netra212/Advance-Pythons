import random 

def run_guess_number(guess_input, answer):
    guess = int(input('guess a number 1~10: '))
    if 0 < guess_input < 11:
        if guess_input == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bro, I said 1~10')
        return False

if __name__ == '__main__':

    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if (run_guess_number(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue