print("Welcome to game of Tic Tac Toe")

row1 = ["M","M","M"]
row2 = ["M","M","M"]
row3 = ["M","M","M"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to mark? ")

x = int(position[0])
y = int(position[1])

selected_row = map[y-1]
selected_row[x-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
