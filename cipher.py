def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # only change letters
            ascii_base = 65 if char.isupper() else 97
            if mode == "encrypt":
                shifted = (ord(char) - ascii_base + shift) % 26
            else:  # decrypt
                shifted = (ord(char) - ascii_base - shift) % 26

            result += chr(shifted + ascii_base)
        else:
            result += char  # keep spaces and symbols unchanged

    return result


print("Caesar Cipher Tool")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose 1 or 2: ")
message = input("Enter your message: ")
shift = int(input("Enter shift value (number): "))

if choice == "1":
    output = caesar_cipher(message, shift, "encrypt")
    print("Encrypted Message:", output)
elif choice == "2":
    output = caesar_cipher(message, shift, "decrypt")
    print("Decrypted Message:", output)
else:
    print("Invalid choice.")
