# OTP.py

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

def main():
    xorString("Darlin dont you go", "and cut your hair!")

if __name__ == "__main__":
    main()