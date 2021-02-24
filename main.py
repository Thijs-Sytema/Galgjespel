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

