cipher_text = ""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def encrypt(original_text, shift_amount):
    global cipher_text
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(encrypted_text, shift_amount):
    real_text = ""
    for letter in encrypted_text:
        shifted_position = alphabet.index(letter) - shift_amount
        real_text += alphabet[shifted_position % 26]
    print(f"Here is the decoded result: {real_text}")

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(encrypted_text=cipher_text, shift_amount=shift)
else:
    print("Please enter 'encode' or 'decode'!")



