import random
print("Welcome to Rock, Paper and Scissors Game! \n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
usr_choice = int(input("Please select your choice? 0 = Rock, 1 = Paper and 2 = Scissors \n"))
print(f"You chose: {image[usr_choice]} \n")
comp_choice = random.randint(0,2)
print(f"Computer Choose: {image[comp_choice]} \n")

if usr_choice >= 3 and usr_choice < 0:
  print("Check your input again. ")
elif usr_choice == 0 and comp_choice == 2:
  print("You Win! ")
elif usr_choice == 2 and comp_choice == 0:
  print("You Lose! ")
elif comp_choice > usr_choice:
  print("You Lose! ")
elif usr_choice > comp_choice:
  print("You Win! ")
elif comp_choice == usr_choice:
  print("Draw!")
