def encrypt(text, shift):
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypt(text, shift):
    # Decryption is just encryption with the negative shift
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? Enter E or D: ").upper()
        
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E or D.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Do you want to process another message? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
