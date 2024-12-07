import base64


def base64_encode(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

# Function to decode a base64 string
def base64_decode(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

# Sample text to encode
text_to_encode = "Hello, Base64 Encoding and decoding!"

# Encode the text to Base64
encoded_text = base64_encode(text_to_encode)

# Print the encoded text
print("Encoded Text: " + encoded_text)

# Decode the encoded text
decoded_text = base64_decode(encoded_text)

# Print the decoded text
print("Decoded Text: " + decoded_text)