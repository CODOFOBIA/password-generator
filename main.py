import random
import string

def password_generator(length):
    pass_char = []
    pass_digit = []
    punctuation = []
    for _ in range(length):
        char = random.choice(string.ascii_letters)
        digit = random.choice(string.digits)
        punc = random.choice(string.punctuation)
        pass_digit.append(digit)
        pass_char.append(char)
        punctuation.append(punc)
    
    password_generated = pass_char + pass_digit + punctuation
    random.shuffle(password_generated)
    password_generated = "".join(password_generated)
    
    return password_generated

passwords = []

while True:
    try:
        length = int(input("Enter the length: "))
        if length > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        
password = password_generator(length)

passwords.append(password)

print(passwords)