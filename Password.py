import random
import string

def generate_password(length):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the all_characters string
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Simple Password Generator!")

    # Input password length
    try:
        length = int(input("Enter the desired password length: "))

        if length < 8:  # Password should be at least 8 characters long
            print("For security reasons, it's recommended to have a password with at least 8 characters.")
            return
        
        # Generate password
        password = generate_password(length)
        
        # Display the password
        print(f"Your generated password is: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
