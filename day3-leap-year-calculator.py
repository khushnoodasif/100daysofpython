year = int(input("Which year do you want to check? \n"))

check1 = year%4
check2 = year%100
check3 = year%400

if check1 == 0:
  if check2 == 0:
    if check3 ==0:
      print("It is a leap year.\n")
    else:
      print("It is not a leap year.\n")
  else:
    print("It is a leap year.\n")
else:
  print("It is not a leap year.\n")
