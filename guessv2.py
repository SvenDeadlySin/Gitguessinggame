# Guess My Number

import random
import time

print("\tWelcome to 'Guess My Number'!")
time.sleep(2)
print("\nI'm thinking of a number between 1 and 50...")
time.sleep(3)
print("Try to guess it in as few attempts as possible...\n")

# setting initial values
the_number = random.randint(1, 50)
guess = int(input("Take a guess: "))
tries = 1
attempts = 6
# guessing loop
while guess != the_number and tries < attempts:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries =+ 1

if tries > attempts - 1:
        print("You did not manage to guess the number!")
elif guess == the_number:
    print("You guessed it! The number was", the_number)
    time.sleep(2)
    print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
        
