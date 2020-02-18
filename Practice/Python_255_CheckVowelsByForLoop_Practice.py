word = input('Enter a world:')
word.lower()
n = len(word)
vowels = 0 #a, e, i, o
#Using for loop
for n in range(len(word)):
    if (word[n] == 'a' or word[n] == 'e' or word[n] == 'i' or word[n] == 'o'):
        vowels += 1
print('Number of vowels: ' + str(vowels))
input('Enter to exit')
