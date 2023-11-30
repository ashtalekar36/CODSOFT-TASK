import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("\nEnter the length of the password: "))
        if length <= 0:
            print("Please enter a valid  length.")
            return
        password = generate_password(length)
        print("The generated Password is :\n", password)
    except ValueError:
        print("Please enter a valid number .")

if __name__ == "__main__":
    main()

