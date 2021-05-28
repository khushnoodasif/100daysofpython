print("Caesar Cipher!")
from day8_caesar_cipher_files import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text,shift):
# 	cipher_text = ""
# 	for letter in text:
# 		position = alphabet.index(letter)
# 		new_position = position + shift
# 		new_letter = alphabet[new_position]
# 		cipher_text += new_letter
# 	print(f"The encoded text: {cipher_text}")
#
# def decrypt(text,shift):
# 	caesar_text = ""
# 	for letter in text:
# 		position = alphabet.index(letter)
# 		new_position = position - shift
# 		caesar_text += alphabet[new_position]
# 	print(f"The decoded text: {caesar_text}")
#
# if direction == "encode":
# 	encrypt(text,shift)
# elif direction == "decode":
# 	decrypt(text,shift)
	
def caesar(text,shift,direction):
	end_text = ""
	if direction == "decode":
		shift *= -1
	for char in text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift
			end_text += alphabet[new_position]
		else:
			end_text += char
	print(f"The {direction}d text: {end_text}")

task_end = False
while not task_end:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift = shift % 26
	caesar(text,shift,direction)

	restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
	if restart == "no":
		task_end = True
		print("Goodbye")
