word = input('Enter a world:')
n = len(word)
word.lower()
vowels = 0 #a, e, i, o
#Using while loop
while n > 0:
    char = word[-1]
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o'):
        vowels += 1
    word = word[0:-1]
    n -= 1
print('Number of vowels: ' + str(vowels))
input('Enter to exit')
