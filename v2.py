
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cypher(input_text, shift_num, mode):
  output = []
  if mode == "decode":
    shift_num = shift_num * -1
  for character in input_text:
    if character in alphabet:
      position = alphabet.index(character)
      newposition = (position + shift_num)%26
      new_char = alphabet[newposition]
    else:
      new_char = character
    output.append(new_char)
    merged = "".join(output)
  print(f"The {mode}d text is {merged}\n")
  
retry = True
print("Welcome to the Caesar Cypher text encryption program !")
while retry == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  cypher(text, shift, direction)
  retry_request = input("Want to continue? Type 'yes' or 'no'.\n")
  if retry_request == "yes":
    retry = True
  elif retry_request == "no":
    retry = False
print("Goodbye")

#Example:
# "hello" encoded with a shift of 5 is "mjqqt"
