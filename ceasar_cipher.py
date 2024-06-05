def c_encrypt(string, step):
    encrypted = ''
    for i in string:
        encrypted += chr((ord(i) - 97 + step) % 26 + 97)
    return encrypted

def c_decrypt(string, step):
    step = step*-1
    decrypted = ''
    for i in string:
        decrypted += chr((ord(i) - 97 + step) % 26 + 97)
    return decrypted

print(c_encrypt('abcdef', 1))
print(c_decrypt('abcdef', 1))
