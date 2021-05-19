print("Welcome to the rollercoaster! \n")
height = int(input("What is your height in cm? \n"))
bill = 0
if height >= 150: 
  print("You can ride! \n")
  age = int(input("For pricing, what is your age? \n"))
  if age < 12:
    bill = 5
    print("Please pay $5. \n")
  elif age <= 18:
    bill = 7
    print("Please pay $7. \n")
  else:
    bill = 12
    print("Please pay $12. \n")
  photo = input("Do you need a photo taken? (Yes/No) \n")
  if photo == "Yes":
    bill += 3
  print(f"Your bill is: ${bill}")
else:
  print("You can not ride! \n")
