class Hangman:
  def __init__(self,word_list,num_lives = 5) -> None:
    self.word_list = word_list
    self.num_lives = num_lives

    self.word = random.choice(self.word_list)
    self.word_guessed = ["_"] * len(self.word)
    self.num_letters = len([letter for letter in set(self.word) if letter not in self.word_guessed])
    self.list_of_guesses = []

  def check_letter(self, letter) -> None: # Method to check the letter 
    letter = letter.lower()
    if letter in self.word:
      print(f"The letter {letter} is in the word to be guessed!")
      letter_index = 0
      for position, char in enumerate(self.word):
          if char == letter:
              letter_index = position
              self.word_guessed[letter_index] = letter
      print(f"Nice! {letter} is in the word!")
      print(f"{self.word_guessed}")
      self.num_letters -= 1
    else:
        self.num_lives -= 1
        print(f"Sorry, {letter} is not in the word.")
        print(f"{self.list_visual[self.num_lives]}")
        print(f"You have {self.num_lives} lives left.")
    self.list_letters.append(letter)
    
  def ask_for_input(self):#Method requesting the input
      while True:
          guess = input("Enter a single letter guess: ")
          if len(guess) != 1 and not guess.isalpha():
              print("Invalid letter. Please, enter a single alphabetical character.")
          elif letter in self.list_letters:
            print(f"{letter} was already tried")
          else:
              self.list_of_guesses.append(guess)
              self.check_guess(guess)

# Defining a function that allows the user to play the game

def play_game(word_list):    
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost')
            print(f'Word was {game.word}')
            print(f'You guessed so far {game.word_guessed}')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_letters == 0:
            print('Congratulations. You won the game')
            print(f'Word was {game.word}')
            print(f'You guessed so far {game.word_guessed}')
            break

# Code to play the game
word_list = ['apple', 'banana', 'pear', 'mango', 'grapefruit']
play_game(word_list)
