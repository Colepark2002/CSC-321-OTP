# OTP.py

import os

used_keys = {}

def xorString(str1, str2):
    if len(str1) != len(str2):
        print("ERR: strings must have same length")
        return -1
    
    xor_res = []
    for i in range(len(str1)):
        xor_char = chr(ord(str1[i]) ^ ord(str2[i]))
        xor_res.append(xor_char)
    xor_res = ''.join(xor_res)
    print(xor_res)
    hex_res = xor_res.encode('utf-8').hex() # convert to bytes then to hex
    print(hex_res)
    return hex_res

def xorBytes(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        print(len(bytes1))
        print(len(bytes2))
        print("ERR: byte sequences must have the same length")
        return -1
    
    xor_res = bytearray(len(bytes1))
    for i in range(len(bytes1)):
        xor_res[i] = bytes1[i] ^ bytes2[i]
    return xor_res

def generate_key(length):
    key = bytearray()
    while len(key) < length:
        key += os.urandom(length - len(key))
    return key

def generate_unique_key(length):
    while True:
        key = generate_key(length)
        key_str = str(key)
        if key_str not in used_keys:
            used_keys[key_str] = True
            return key

def otpEncryption(plaintext_file, ciphertext_file):
    # Read plaintext from file
    with open(plaintext_file, 'rb') as file:
        plaintext = file.read().strip()
    
    # Generate random key
    key = generate_unique_key(len(plaintext))
    
    # Perform XOR operation to encrypt plaintext
    ciphertext = xorBytes(plaintext, key)
    
    # Write ciphertext to file
    with open(ciphertext_file, 'wb') as file:
        file.write(ciphertext)
    
    # Verify decryption
    decrypted_text = xorBytes(ciphertext, key)
    
    # Check if decryption matches original plaintext
    if decrypted_text == plaintext:
        print("Decryption successful. Original plaintext recovered.")
    else:
        print("Decryption failed. Original plaintext not recovered.") 
            
def main():
    xorString("Darlin dont you go", "and cut your hair!")
    otpEncryption("TestOTP.txt", "ciphertext_file")

if __name__ == "__main__":
    main()