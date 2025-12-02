import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Password too short. Minimum is 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)
    print("\nYour generated password:")
    print(password)

if __name__ == "__main__":
    main()
