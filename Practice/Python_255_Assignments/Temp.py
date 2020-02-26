import string
def encode(sentence, distance):
    words = sentence.split(' ')
    result = ''
    for count in range(len(sentence)):
        char = sentence[count]
        if char in string.ascii_lowercase:
           char = chr((ord(char) + distance - 65) % 26 + 65)
           result += char
    return result

print(encode("abcd", 5))
