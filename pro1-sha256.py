import hashlib


def hash_password(password):
    password_bytes=password.encode('utf-8')
    hash_obj=hashlib.sha256(password_bytes)
    password_hash=hash_obj.hexdigest()
    return password_hash
password=input("Enter password:")
hashed_password=hash_password(password)
print(f"Hashed password:{hash_password(password)}")
