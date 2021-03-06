
import random

word_list = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialtieit","verzekering","universiteit","heesterperk"]

def get_word(word_list):
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = [] 
  guessed_words = []
  tries = 6
  print("Het spel gaat beginnen!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Raad een letter of woord: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("Je hebt deze letter al geprobeerd: ", guess, "!")
    elif guess not in word:
      print(guess, "is niet in het woord :(")
      tries -= 1
      guessed_letters.append(guess)
    else:
      print("Goed zo,", guess, "zit in het woord!")
      guessed_letters.append(guess)
      word_as_list = list(word_completion)
      indices = [i for i, letter in enumerate(word) if letter == guess]
      for index in indices:
        word_as_list[index] = guess
      word_completion = "".join(word_as_list)
      if "_" not in word_completion:
        guessed = True
  elif len(guess) == len(word) and guess.isalpha():
    if guess in guessed_words:
      print("Je hebt deze letter al geprobeerd: ", guess, "!")
    elif guess != word:
      print(guess,"is helaas niet het woord :(")
      tries -= 1
      guessed_words_apends(guess)
  else:
    guessed = True
    word_completion = word
else:
  print("ongeldige input")
print(display_hangman(tries))
print(word_completion)
print("\n")

if guessed:
  print("Goed zo, je hebt het woord geraden!")
else:
  print("Helaas, je levens zijn op. Het woord was " + word +" . Volgende keer beter!"

def display_hangman(tries):
  stages = ['''
     +---+
         |
         |
         |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
     ===''', '''
   +---+
   O   |
  /|\  |
       |
     ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
       ===''']
      
return stages[tries]

def main():
  word = get_word(word_list)
  play(word)
  while input("Opnieuw spelen? (J/N) ").upper() == "J":
    word = get_word(word_list)
    play(word)

if  name == " main ":
  main()
