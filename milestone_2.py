import random

word_list = ['apple', 'banana', 'pear', 'mango', 'grapefruit']
print(word_list)

word = random.choice(word_list)

guess = input("Please Enter a single letter guess: ")
if len(guess) == 1:
    print("Good guess!.")
else:
    print("Oops! That is not a valid input.")

