import random
from day7-hangman-game-files import word_list, logo, stages

print("Welcome to Hangman Game! \n")
print(logo + "\n")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
	display += "_"
	
end_of_game = False
while not end_of_game:
  guess_word = input("Guess a letter: ").lower()
  if guess_word in display:
    print(f"{guess_word} already guessed! \n")
    
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess_word:
      display[position] = letter
      
  if guess_word not in chosen_word:
    print(f"{guess_word} not in the word. You lose a life. \n")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("Game Over! \n")
      
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print("You Win! \n")
  print(stages[lives])
