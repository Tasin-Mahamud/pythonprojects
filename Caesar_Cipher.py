list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt \t")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


def encrypt(txt,sft):
    cipher_text = ""
    for alphabet in txt:
        position = list_of_letters.index(alphabet)
        new_position = position + sft
        new_Letter = list_of_letters[new_position]
        cipher_text += new_Letter
    print( "Your encrypted text is",cipher_text)

def decrypt(txt,sft):
    plain_text = ""
    for alphabet in txt:
        position = list_of_letters.index(alphabet)
        new_position = position - sft
        new_Letter = list_of_letters[new_position]
        plain_text += new_Letter
    print( "Your decrypted text is",plain_text)


if(direction == "encode"):
    encrypt(text,shift)

elif(direction == "decode"):
    decrypt(text, shift)



