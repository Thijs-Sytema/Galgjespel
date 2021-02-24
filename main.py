word_list = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialtieit","verzekering","universiteit","heesterperk"]

def get word(word_list):
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = "_" len(word)
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
    

