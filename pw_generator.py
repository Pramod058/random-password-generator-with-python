import string
import random
characters = list(string.ascii_letters + string.digits + string.punctuation)
def generate():
    try:
        length = int(input("Enter the length of the password:"))
    except:
        print("Enter valid integer  number")
        return
    chars = []
    for i in range(length):
        chars.append(random.choice(characters))
    random.shuffle(chars)
    password = "".join(chars)
    print(password)


while True:
    generate()