from cryptography.fernet import Fernet

# Function to generate a new Fernet key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message using a provided key
def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message using a provided key
def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# Function to display the menu and handle user inputs
def menu():
    print("Data Encryption Menu")
    print("1. Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")

    while True:
        choice = input("Select an option: ")
        if choice == '1':
            # Generate and display a new key
            key = generate_key()
            decoded = key.decode()
            print(f"Generated Key: {decoded}")
            continue
        elif choice == '2':
            # Encrypt a message using a provided key
            inputKey = input("Enter key: ")
            if inputKey == decoded:
                encoded = inputKey.encode()
                message = input("Enter message to encrypt: ")
                encrypted_message = encrypt_message(encoded, message)
                print(f"Encrypted Message: {encrypted_message.decode()}")
            else:
                print("Key is incorrect")
            continue
        elif choice == '3':
            # Decrypt a message using a provided key
            key = input("Enter key: ").encode()
            encrypted_message = input("Enter message to decrypt: ").encode()
            decrypted_message = decrypt_message(key, encrypted_message)
            print(f"Decrypted Message: {decrypted_message}")
            continue
        elif choice == 'stop':
            # Exit the menu
            break
        else:
            # Handle invalid options
            print("Invalid option")

if __name__ == "__main__":
    menu()
