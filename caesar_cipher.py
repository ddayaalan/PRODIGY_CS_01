def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    # Adjust the shift based on the mode
    if mode == "decrypt":
        shift = -shift
    
    # Process each character
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # If character is not a letter, leave it as it is
            result += char

    return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

# Check mode and display result
if mode == "encrypt":
    encrypted_text = caesar_cipher(message, shift, mode="encrypt")
    print("Encrypted message:", encrypted_text)
elif mode == "decrypt":
    decrypted_text = caesar_cipher(message, shift, mode="decrypt")
    print("Decrypted message:", decrypted_text)
else:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
