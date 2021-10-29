import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_len = len(names)
ran_no = random.randint(0,name_len-1)
print(f"{names[ran_no]} will have to pay today")
