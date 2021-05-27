print("Calculate number of cans needed to paint a wall. \n")

def paint_calc(height, width, cover):
	number_of_cans = round((height * width) / cover)
	print(f"Number of cans needed: {number_of_cans}")
	
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
