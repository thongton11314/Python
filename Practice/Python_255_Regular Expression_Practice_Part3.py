"""Perfect
Ed Sheeran"""

import re

lyric = """I found a love for me
Darling just dive right in
And follow my lead
Well I found a girl beautiful and sweet 
I never knew you were the someone waiting for me
'Cause we were just kids when we fell in love

Not knowing what it was
I will not give you up this time
But darling, just kiss me slow, your heart is all I own
And in your eyes you're holding mine

Baby, I'm dancing in the dark with you between my arms
Barefoot on the grass, listening to our favorite song
When you said you looked a mess, I whispered underneath my breath
But you heard it, darling, you look perfect tonight

Well I found a woman, stronger than anyone I know
She shares my dreams, I hope that someday I'll share her home
I found a love, to carry more than just my secrets
To carry love, to carry children of our own
We are still kids, but we're so in love
Fighting against all odds
I know we'll be alright this time
Darling, just hold my hand
Be my girl, I'll be your man
I see my future in your eyes

Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
When I saw you in that dress, looking so beautiful
I don't deserve this, darling, you look perfect tonight woo

Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
I have faith in what I see
Now I know I have met an angel in person
And she looks perfect
I don't deserve this
I can not quit to love my queen many many*time """

# This function will return a list contain a word that not appear twice
def nonDuplicateWordInList(listOfWord):
    nonDuplicatedList = []
    for eachWord in listOfWord:
        if eachWord not in nonDuplicatedList:
            nonDuplicatedList.append(eachWord)
    return nonDuplicatedList

# Write functions using regex to perform the following search and to print out every word from the file that matches the requirement. 
def search(lyric):

    # has a 'q'
    word = re.findall(r'\w*q\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has a \'q\':' + str(words))
    print()

    # has 'th'  
    word = re.findall(r'\w*th\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has a \'th\':' + str(words))
    print()

    # has an 'q' or a 'Q'
    word = re.findall(r'\w*[qQ]\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has a \'q\' or \'Q\':' + str(words))
    print()

    # has a '*' in it
    word = re.findall(r'\w*[*]+\w*',lyric)
    words = nonDuplicateWordInList(word)
    print('- Has a \'*\' in it:' + str(words))
    print()

    # starts with an 'q' or an 'Q'
    word = re.findall(r'[qQ]\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- Starts with an \'q\' or \'Q\':' + str(words))
    print()

    # has both 'a' and 'e' in it
    word = re.findall(r'\w*a\w*e\w*|\w*e\w*a\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has both \'a\' and \'e\' in it:' + str(words))
    print()

    # has an 'a' and somewhere later an 'e'
    word = re.findall(r"\w*[a]\w*[e]\w*", lyric)
    words = nonDuplicateWordInList(word)
    print('- has an \'a\' and somewhere later an \'e\':' + str(words))
    print()

    # does not have an 'a'
    word = re.findall(r'\b[^a\s]+\b', lyric)
    words = nonDuplicateWordInList(word)
    print('- Does not have an \'a\':' + str(words))
    print()

    # does not have an 'a' nor 'e'  
    word = re.findall(r'\b[^ae\s]+\b', lyric)
    words = nonDuplicateWordInList(word)
    print('- Does not have an \'a\' nor \'e\':' + str(words))
    print()

    # has an 'a' but not 'e'
    word = re.findall(r'\b[^e\s]+\b', lyric)
    words = nonDuplicateWordInList(word)
    print('- has an \'a\' but not \'e\':' + str(words))
    print()

    # has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
    word = re.findall(r"\w*[aeiou]{2,}[\w\S]*", lyric)
    words = nonDuplicateWordInList(word)
    print('- Has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear":' + str(words))
    print()

    # has at least 3 vowels
    word = re.findall(r'\w*[aeiou]+\w*[aeiou]+\w*[aeiou]+[\w\S]*\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has at least 3 vowels:' + str(words))
    print()

    # has at least 6 characters
    word = re.findall(r'\w{6,}', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has at least 6 characters:' + str(words))
    print()

    # has at exactly 6 characters
    word = re.findall(r'\b\w{6}\b', lyric)
    words = nonDuplicateWordInList(word)
    print('- Has at exactly 6 characters:' + str(words))
    print()

    # all the words with either 'Bar' or 'Baz' in them
    word = re.findall(r'\bBa[rz]\w*', lyric)
    words = nonDuplicateWordInList(word)
    print('- All the words with either \'Bar\' or \'Baz\' in them:' + str(words))
    print()

    # all the rows with either 'apple pie' or 'banana pie' in them
    print("- All the rows with either 'apple pie' or 'banana pie' in them")
    listOfSentences = re.findall(r'.+', lyric)
    for eachSentence in listOfSentences:
        matches = re.findall(r'apple\spie|banana\spie', eachSentence)
        if matches:
            print("  Line " + str(listOfSentences.index(eachSentence)))
        if listOfSentences.index(eachSentence) == len(listOfSentences) - 1:
            print("  Not match any")
    print()

    # for each row print if it was apple or banana pie?
    print("- For each row print if it was apple or banana pie?")
    listOfSentences = re.findall(r'.+', lyric)
    for eachSentence in listOfSentences:
        matches = re.findall(r'apple|banana\spie', eachSentence)
        if matches:
            print("  Line " + str(listOfSentences.index(eachSentence)))
        if listOfSentences.index(eachSentence) == len(listOfSentences) - 1:
            print("  Not match any")
    print()

    # Bonus: Print if the same word appears twice in the same line
    print("- Print if the same word appears twice in the same line")
    listOfSentences = re.findall(r'.+', lyric) #Seperate the sentence in list
    for index, eachSentence in enumerate(listOfSentences): #Loop through the list to find the words appears twice
        matches = re.findall(r'(\b\w[^\s]+\b).+\1\b', eachSentence)
        if matches:
            print("  Line " + str(index + 1) + " in Lyric:" + str(matches))
    print()
    
    # Bonus: has a double character (e.g. 'oo')
    word = re.findall(r"\w*o{2}\w*", lyric)
    words = nonDuplicateWordInList(word)
    print('- Has a double character (e.g. \'oo\'):' + str(words))
    print()
search(lyric)
print("End")
