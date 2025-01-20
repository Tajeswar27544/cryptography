# Shift Cipher (Caesar Cipher)
def shift_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def shift_cipher_decrypt(text, shift):
    return shift_cipher_encrypt(text, -shift)

# Rail Fence Cipher
def rail_fence_encrypt(text, rails):
    # Create a rail fence matrix with `rails` rows
    rail = [['\n' for i in range(len(text))] for j in range(rails)]
    direction = 1  # Start by moving downwards
    row, col = 0, 0

    for char in text:
        rail[row][col] = char
        col += 1
        row += direction

        # Change direction if we hit the top or bottom row
        if row == 0 or row == rails - 1:
            direction = -direction

    # Read the matrix row by row
    encrypted_text = ''.join([''.join(rail[i]) for i in range(rails)])
    return encrypted_text

def rail_fence_decrypt(text, rails):
    # Create a rail fence matrix with `rails` rows
    rail = [['\n' for i in range(len(text))] for j in range(rails)]
    direction = 1  # Start by moving downwards
    row, col = 0, 0

    # Mark positions in the rail matrix
    for i in range(len(text)):
        rail[row][col] = '*'
        col += 1
        row += direction
        if row == 0 or row == rails - 1:
            direction = -direction

    # Fill the rail matrix with the ciphertext
    idx = 0
    for i in range(rails):
        for j in range(len(text)):
            if rail[i][j] == '*':
                rail[i][j] = text[idx]
                idx += 1

    # Read the matrix row by row
    decrypted_text = ""
    row, col = 0, 0
    direction = 1
    for i in range(len(text)):
        decrypted_text += rail[row][col]
        col += 1
        row += direction
        if row == 0 or row == rails - 1:
            direction = -direction
    return decrypted_text

# Product Cipher: Using Shift Cipher and Rail Fence Cipher
def product_cipher_encrypt(text, shift, rails):
    # First, apply the Shift Cipher (Caesar Cipher)
    shift_encrypted = shift_cipher_encrypt(text, shift)
    # Then apply the Rail Fence Cipher
    rail_encrypted = rail_fence_encrypt(shift_encrypted, rails)
    return rail_encrypted

def product_cipher_decrypt(text, shift, rails):
    # First, apply the Rail Fence Cipher decryption
    rail_decrypted = rail_fence_decrypt(text, rails)
    # Then apply the Shift Cipher decryption
    shift_decrypted = shift_cipher_decrypt(rail_decrypted, shift)
    return shift_decrypted

# User input
def main():
    print("Welcome to the Product Cipher Encryption/Decryption!")
    
    # Taking user input
    plaintext = input("Enter the plaintext: ")
    shift_value = int(input("Enter the shift value for Shift Cipher (e.g., 3): "))
    rail_count = int(input("Enter the number of rails for Rail Fence Cipher (e.g., 3): "))

    print(f"\nOriginal Plaintext: {plaintext}")

    # Encrypt using Product Cipher
    encrypted_text = product_cipher_encrypt(plaintext, shift_value, rail_count)
    print(f"Encrypted Text (Product Cipher): {encrypted_text}")

    # Decrypt using Product Cipher
    decrypted_text = product_cipher_decrypt(encrypted_text, shift_value, rail_count)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == '__main__':
    main()
