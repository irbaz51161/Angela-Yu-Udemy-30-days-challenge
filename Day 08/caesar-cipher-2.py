alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(txt, sft):
    encrypt_word = ""
    for letter in txt:
        pos_letter = alphabet.index(letter)
        encrypt_letter = pos_letter + sft
        encrypt_word += alphabet[encrypt_letter]

    print(f"Encrypted word for \"{txt}\" is \"{encrypt_word}\".")
    return encrypt_word

def decrypt(dd):
    decrypt_word = ""
    for letter in dd:
        pos_letter = alphabet.index(letter)
        decrypt_letter = pos_letter - shift
        decrypt_word += alphabet[decrypt_letter]

    print(f"Decrypted word for \"{dd}\" is \"{decrypt_word}\".")

e = encrypt(text, shift)
d = decrypt(e)