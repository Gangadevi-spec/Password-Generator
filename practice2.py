import random
import string

def password_generate(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    Password = ''.join(random.choices(characters, k=length))
    return Password

try:
    length=int(input("Enter the desired length :"))
    password1=password_generate(length)
    print(password1)
except ValueError:
    print("Enter valid number") 