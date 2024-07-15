import random
import string


def generate_password(length, complexity):
    characters = ""
    if 'l' in complexity:
        characters += string.ascii_lowercase
    if 'u' in complexity:
        characters += string.ascii_uppercase
    if 'd' in complexity:
        characters += string.digits
    if 's' in complexity:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_complexity():
    print("\nPassword complexity options:")
    print("l - Include lowercase letters")
    print("u - Include uppercase letters")
    print("d - Include digits")
    print("s - Include symbols")
    return input("Enter desired complexity (e.g., 'luds' for all options): ").lower()


def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Password length should be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    complexity = get_complexity()

    password = generate_password(length, complexity)
    print(f"\nYour generated password is: {password}")


if __name__ == "__main__":
    main()