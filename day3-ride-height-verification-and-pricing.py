print("Welcome to the rollercoaster! \n")
height = int(input("What is your height in cm? \n"))
if height >= 150: 
  print("You can ride! \n")
  age = int(input("For pricing, what is your age? \n"))
  if age <= 18:
    print("Please pay $7 \n")
  else:
    print("Please pay $12 \n")
else:
  print("You can not ride! \n")
