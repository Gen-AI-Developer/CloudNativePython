# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48
import random
print("I am thinking of a number between 0 and 9...")
random_number = random.randint(0, 9)
allowed_attempts: int = 5;
guess = int(input("Enter a guess: "))
while True:
    if allowed_attempts > 0:
        if guess == random_number:
            print("Congrats! The number was: ", random_number)
            break
        elif guess > random_number:
            print("Your guess is too high")
            allowed_attempts -= 1
        else:
            print("Your guess is too low")
            allowed_attempts -= 1
    elif allowed_attempts == 0:
        print("You have no more attempts left.")
        print("You have ", allowed_attempts, " attempts left")
        print("Your guess is: ", guess)
        print("The number was: ", random_number)
        break
    else:
        print("You have ", allowed_attempts, " attempts left")
        guess = int(input("Enter a new number: "))
        continue
    guess = int(input("Enter a new number: "))
    continue


    
