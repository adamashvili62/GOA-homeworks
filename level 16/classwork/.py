count = 0
while count < 10:
    print("Your Name")
    count += 1


# 2

def guess_number():
    correct_number = 7
    guess = None
    while guess != correct_number:
        guess = int(input("Guess the number: "))
        if guess == correct_number:
            print("Correct!")
        else:
            print("Try again!")
guess_number()