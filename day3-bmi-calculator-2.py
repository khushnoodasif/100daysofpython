print("Calculate your BMI using your weight and height. \n")
w = float(input("What is your weight in kg? \n"))
h = float(input("what is your height in m? \n"))
BMI = round(w/h**2)
if BMI < 18.5:
  print(f"Your BMI is: {BMI}, You are underweight.\n")
elif BMI < 25:
    print(f"Your BMI is: {BMI}, You are normal weight. \n")
elif BMI < 30:
    print(f"Your BMI is: {BMI}, You are over weight. \n")
elif BMI < 35:
    print(f"Your BMI is: {BMI}, You are obese. \n")
else:
  print(f"Your BMI is: {BMI}, You are clinically obese. \n")
