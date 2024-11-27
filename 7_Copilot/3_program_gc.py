from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    key = RSA.generate(2048)
    public_key = key.publickey()
    public_key_exported = public_key.export_key()

    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key_exported)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_result = cipher.encrypt(result.encode())
    return base64.b64encode(encrypted_result).decode()


def decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Choose (e)ncrypt or (d)ecrypt: ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift number: "))
    if choice == 'e':
        print("Encrypted:", caesar_cipher_encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted:", decrypt(text, shift))
    else:
        print("Invalid choice.")