
import random

actual_number = random.randint(1, 100)
print('Welcome to the number guessing game')
print('I am thinking of a number between 1 and 100')

difficulty_level = input('choose difficulty: Type "easy" or "hard"')

def game(a):
  print(f"you have {a-1} attempts guess the correct number")
  is_guessed = False
  for i in range(1, a):
      guess = int(input('Make a guess: '))
      
      if actual_number > guess:
          print('Too low')
          print('guess again')
          if i<a-1: 
              print(f'you have {a-1-i} attempts guess the correct number')

      elif actual_number == guess:
          print(f"You got it! The actual answer was {actual_number}")
          is_guessed = True
          break
      else:
          print('Too high')
          print('guess again')
          if i<a-1: 
              print(f'you have {a-1-i} attempts guess the correct number')
  if is_guessed ==False:
      print('you have run out of guesses')
  

if difficulty_level == 'easy':
  game(11)
else:
  game(6)
  
