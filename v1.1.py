
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cypher(input_text, shift_num, mode):
  output = []
  if mode == "decode":
    shift_num = shift_num * -1
  for letter in input_text:
    position = alphabet.index(letter)
    newposition = (position + shift_num)%26
    new_char = alphabet[newposition]
    output.append(new_char)
    merged = "".join(output)
  print(f"The {mode}d text is {merged}")

cypher(text, shift, direction)

#Example:
# "hello" encoded with a shift of 5 is "mjqqt"
