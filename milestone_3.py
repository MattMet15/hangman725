def ask_for_input():
  guess.lower()
  ## Loop to chek if the input from the user is an alphabetical character - will use isalpha
  while True:
    guess = input("Please Guess a letter: ")
    if guess.isalpha() == True:
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
  if guess in word:
    print(f"Good guess!{guess} is in the word")
  else:
    print(f"Sorry, {guess} is not in the word. Try again!")
