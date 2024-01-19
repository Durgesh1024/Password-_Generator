import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count=5, length=12):
    
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

def main():
    print("Password Generator")

    try:
        # Get user input for password length and count
        length = int(input("Enter the desired password length: "))
        count = int(input("Enter the number of passwords to generate: "))

        # Validate user input
        if length <= 0 or count <= 0:
            print("Please enter valid values for length and count.")
            return

        # Generate passwords
        passwords = generate_multiple_passwords(count, length)

        # Display generated passwords
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
