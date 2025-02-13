#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess= random.randint(1,100)
def guessing():
  user_guess = int(input("Make a guess: "))
  if user_guess == guess:
    global game_over
    print(f"You got it! The answer was {guess}.")
    game_over = True
  elif user_guess > guess:
    print("Too high.")
  elif user_guess < guess:
    print("Too low.")
  else:
    print("Invalid input.")
game_over = False
if difficulty == "easy":
  attempt=10
else:
  attempt=5
while not game_over:
  print(f"You have {attempt} attempts remaining to guess the number.")
  guessing()
  attempt-=1
  if attempt==0:
    game_over=True
    print("You've run out of guesses, you lose.")
  else:
    print("Guess again.")
  


 