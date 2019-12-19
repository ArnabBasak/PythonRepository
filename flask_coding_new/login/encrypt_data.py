from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
original_text = (bytes(input('enter text'),"utf-8"))
print(original_text)
encoded_text = cipher_suite.encrypt(original_text)
print(encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print(str(decoded_text))
