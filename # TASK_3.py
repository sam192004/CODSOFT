import random
import string
def password_Generator(length):
    characters = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Enter a positive character")
            return
        password = password_Generator(length)
        print("Generated password:", password)
    except ValueError:
        print("Enter a valid integer for the length.")
if __name__ == "__main__":
    main()
