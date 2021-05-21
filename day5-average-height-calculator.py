print("Average Height Calculator!")

heights = input("Input a list of heights ").split()
for n in range(0, len(heights)):
  heights[n] = int(heights[n])

total_height = 0 
for height in heights:
  total_height += height

total_no = 0
for students in heights:
  total_no += 1

average_height = round(total_height / total_no)
print(f"Average height: {average_height}")
