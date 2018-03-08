import random

hangMan = ['''
    +---+
    |   |
        |
        |
        |
        |
=========
''',
''' 
    +---+
    |   |
    O   |
        |
        |
        |
=========
''',
'''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
''',
'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
''',
'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
''',
'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
''',
'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
''']
  
animals = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
  
foods = 'jerky/steak/creamed corn/hot dog/Crab cake/Meatloaf/Peanut butter/pizza/ice cream/Hamburger/Waffle/Apple sauce/Cheese/apple'.split('/')

heros = 'Spider-man/irom man/super man/hulk/black panther/black widow/green arrow/thor/vision/flash/firestorm/iron fist/static'.split('/')
  

categoryset = heros

def category():
  global categoryset
  print ('What category would you like to do? (Type a, b, or c)')
  print ('A. Animals')
  print ('B. Foods')
  print ('C. Super Heros')
  
  categoryPicked = input('Category:')
  
  while categoryPicked != 'a' and categoryPicked != 'b' and categoryPicked != 'c':
    print ('Sorry that was not an option.')
    categoryPicked = input('What category would you like to do? (Type a, b, or c)')
  
  if categoryPicked == 'a':
    categoryset = animals
  elif categoryPicked == 'b':
    categoryset = foods
  elif categoryPicked == 'c':
    categoryset = heros

def main():
  
  stillPlaying =True
  
  while stillPlaying:
  
    secretWord = (random.choice(categoryset)).lower()
    attempts = 0
    guessed = ""
    given = " -"
    lettersNeeded = len(secretWord)
    lettersCorrect = 0
  
    while attempts < 6 and lettersCorrect != lettersNeeded:
      
      lettersCorrect = 0
      
      print (hangMan[attempts])
      
      for letter in secretWord:
        if letter in guessed or letter in given:
          lettersCorrect += 1
          print (" ", (letter).upper(), sep="", end="")
        else:
          print (" _", end="")
          
      print ('\n')
      print ('Attempts left:', 6 - attempts)
      print ('Guesses: ', guessed, sep="")
      print ("")
      if lettersCorrect != lettersNeeded:
        guess = input('Guess:')
        while len(guess) > 1 or guess in guessed:
          print ('Sorry you can only enter one letter and you can not guess the same letter twice.')
          guess = input('Guess:')
        guessed += guess
        if guess not in secretWord:
          attempts +=1
      
    if attempts == 6:
      print (hangMan[6])
      print ('Game Over. The word was ', secretWord, '.', sep="")
      
    elif lettersCorrect == lettersNeeded:
      print ('')
      print ('Congrats You Guessed The Word!')
      
    answer = input('Would you like to play again? (Type y or n)')
    while answer != 'n' and answer != 'y':
      print ('Sorry that was not an option.')
      answer = input('Would you like to play again? (Type y or n)')
    if answer == 'n':
      stillPlaying = False
    elif answer == 'y':
      answer2 = input('Would you like to change categories? (Type y or n)')
      while answer2 != 'n' and answer != 'y':
        print ('Sorry that was not an option.')
        answer2 = input('Would you like to change categories? (Type y or n)')
      if answer2 == 'y':
        category()


def intro():
  print ('Welcome to the game hang man.')
  category()
  main()


intro()






























