def encode(sentence, distance):
    words = sentence.split(' ')
    result = ''
    for count in range(len(sentence)):
        char = sentence[count]
        # Encrypt uppercase characters in plain text
        if char.isspace():
            result += char
        else:
            if (char.isupper()):
                result += chr((ord(char) + distance - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + distance - 97) % 26 + 97)
    return result

def decode(sentence, distance):
    words = sentence.split(' ')
    result = ''
    for count in range(len(sentence)):
        char = sentence[count]
        # Encrypt uppercase characters in plain text
        if char.isspace():
            result += char
        else:
            if (char.isupper()):
                result += chr((ord(char) - distance - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) - distance - 97) % 26 + 97)
    return result

print(decode(encode("Thong Ton", 5), 5))
print(decode(encode("Thanh Ton", 5), 5))
print(decode(encode("Diep Ton", 5), 5))
print(decode(encode("Bao Tran", 5), 5))
print(decode(encode("Linh Nguyen", 5), 5))
print(decode(encode("Nghia Le", 5), 5))
print(decode(encode("Thinh Le", 5), 5))






