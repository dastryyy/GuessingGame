import random

# on initialization
num = random.randrange(1, 50)
chances_left = 5


def out_of_range(v):
    if v < 1 or v > 50:
        return True
    else:
        return False


def is_close(n, v):
    if abs(n - v) <= 5:
        return True
    else:
        return False


def give_hints(n, v):
    if is_close(n, v):
        print("You are VERY close!")

    if v < n:
        # aim higher
        print("You might want to guess higher.")
    elif v > n:
        # aim lower
        print("Try guessing lower!")
    return


print("Hello there!")
print("I'm thinking of a number between 1 and 50... can you guess what it is in %d tries?" % chances_left)
while True:
    print("CHANCES LEFT:", chances_left)
    try:
        val = int(input("Enter your best guess here: "))

        if out_of_range(val):
            print("That's out of bounds! Try again.")
        else:
            if val == num:
                print("Congratulations! You have guessed correctly!")
                print("Thanks for playing!")
                quit()
            else:
                chances_left -= 1
                if chances_left > 0:
                    give_hints(num, val)
            if chances_left == 0:
                print("Oops! You're all out of chances; better luck next time!")
                print("Correct answer was %d; thanks for playing!" % num)
                quit()
    except ValueError:
        print("Please type a number between 1 and 50.")
