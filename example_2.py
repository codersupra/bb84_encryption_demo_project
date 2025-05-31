from bb84 import generate_bb84_key
from fernet_crypto import bb84_key_to_fernet_key, encrypt_message, decrypt_message

bb84_key = generate_bb84_key(target_length=128, register_size=5)
print("BB84 Key:", ''.join(map(str, bb84_key)))

fernet_key = bb84_key_to_fernet_key(bb84_key)
print("Fernet Key:", fernet_key.decode())

# Encrypt a message
plaintext = "HELLO" # longer text messages can be used
token = encrypt_message(plaintext, fernet_key)
print("Encrypted Token:", token)

# Decrypt the message
decrypted_message = decrypt_message(token, fernet_key)
print("Decrypted Message:", decrypted_message)