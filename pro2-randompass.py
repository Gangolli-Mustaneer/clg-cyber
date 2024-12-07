import random
import string


def generate_passwod(length=8):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_characters)for i in range(length))
    return password
password_length_str=input("input the desired legth of your password:")
if password_length_str:
    password_legth=int(password_length_str)
else:
    password_legth=8
password=generate_passwod(password_legth)
print(f"Generated password is:{password}")