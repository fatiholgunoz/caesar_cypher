
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(input_text,shift_num):
  encrypted = []
  for letter in input_text:
    position = alphabet.index(letter)
    newposition = (position + shift_num)%26
    new_char = alphabet[newposition]
    encrypted.append(new_char)
    merged = "".join(encrypted)
  print(f"The encoded text is {merged}")

def decrypt(input_text,shift_num):
  decrypted = []
  for letter in input_text:
    position = alphabet.index(letter)
    newposition = (position - shift_num)%26
    new_char = alphabet[newposition]
    decrypted.append(new_char)
    merged = "".join(decrypted)
  print(f"The decoded text is {merged}")

if direction=="encode":
  encrypt(text,shift)
elif direction=="decode":
  decrypt(text,shift)
else:
  print("Please type either *encrypt* or *decrypt*")
  
    #plain_text = "hello"
    #shift = 5
    #print output: "The encoded text is mjqqt"
