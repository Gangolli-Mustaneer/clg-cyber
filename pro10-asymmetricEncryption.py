import binascii

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Generate RSA key pair
keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()

# Export public and private keys
pubkeyPEM = pubKey.exportKey()
privkeyPEM = keyPair.exportKey()

# Encryption
msg = b'Welcome to AIMCA'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

# Decryption
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted:", decrypted.decode('utf-8'))