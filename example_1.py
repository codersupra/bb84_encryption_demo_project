from bb84 import generate_bb84_key

# Example message
plaintext = "HELLO"

binary_plaintext = ''.join(format(ord(c), '08b') for c in plaintext)
print("Binary Plaintext:", binary_plaintext)

bb84_key = generate_bb84_key(target_length=len(binary_plaintext), register_size=5)
print("BB84 Key:         ", ''.join(str(bit) for bit in bb84_key))

# Encryption
ciphertext = ''.join(
    str(int(binary_plaintext[i]) ^ int(bb84_key[i]))
    for i in range(len(binary_plaintext))
)
print("Ciphertext:       ", ciphertext)

# Decryption
decrypted_binary = ''.join(
    str(int(ciphertext[i]) ^ int(bb84_key[i]))
    for i in range(len(ciphertext))
)
print("Decrypted Binary: ", decrypted_binary)

decrypted_text = ''.join(
    chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8)
)
print("Decrypted Text:   ", decrypted_text)
