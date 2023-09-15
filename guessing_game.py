import random
import time

print("Greetings, welcome to the number guessing game! Please input a number between 1 and 100.")
guess = int(input("What is your guess?: "))
time.sleep(3)
print("Picking a number...")
time.sleep(2.5)
correct_number = random.randint(1, 100)

guess_count = 1
while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong you need to guess higher. What is your guess?: "))
    else:
        guess = int(input("Wrong you need to guess lower. What is your guess?: "))
    
print(f'You got the right answer which is {correct_number} :). It took you {guess_count} guess(es).')