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
I don't deserve this, darling, you look perfect tonight

Baby, I'm dancing in the dark, with you between my arms
Barefoot on the grass, listening to our favorite song
I have faith in what I see
Now I know I have met an angel in person
And she looks perfect
I don't deserve this
You look perfect tonight
Quit are out of quin many*time """
 
# Write functions using regex to perform the following search and to print out every word from the file that matches the requirement. 
def search(lyric):

    # has a 'q'
    word = re.findall(r'\w*q\w*', lyric)
    print('- Has a \'q\':' + str(word))
    print()

    # has 'th'  
    word = re.findall(r'\w*th\w*', lyric)
    print('- Has a \'th\':' + str(word))
    print()

    # has an 'q' or a 'Q'
    word = re.findall(r'\w*[qQ]\w*', lyric)
    print('- Has a \'q\' or \'Q\':' + str(word))
    print()

    # has a '*' in it
    word = re.findall(r'\w*[*]\w*',lyric)
    print('- Has a \'*\' in it:' + str(word))
    print()

    # starts with an 'q' or an 'Q'
    word = re.findall(r'\b[qQ]\w*', lyric)
    print('- Starts with an \'q\' or \'Q\':' + str(word))
    print()

    # has both 'a' and 'e' in it

    # has an 'a' and somewhere later an 'e'
    word = re.findall(r"\w*a\w*e\w*", lyric)
    print('- has an \'a\' and somewhere later an \'e\':' + str(word))
    print()

    # does not have an 'a'

    # does not have an 'a' nor 'e' 

    # has an 'a' but not 'e'

    # has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
    word = re.findall(r"\w*[aeiou]{2,}\w*", lyric)
    print('- has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear":' + str(word))
    print()

    # has at least 3 vowels
    word = re.findall(r'\w*[aeiou]{3,}\w*', lyric)
    print('- has at least 3 vowels:' + str(word))
    print()

    # has at least 6 characters
    word = re.findall(r'\w{6,}', lyric)
    print('- Has at least 6 characters:' + str(word))
    print()

    # has at exactly 6 characters
    word = re.findall(r'\b\w{6}\b', lyric)
    print('- Has at exactly 6 characters:' + str(word))
    print()

    # all the words with either 'Bar' or 'Baz' in them
    word = re.findall(r'\bBa[rz]\w*', lyric)
    print('- All the words with either \'Bar\' or \'Baz\' in them:' + str(word))
    print()

    # all the rows with either 'apple pie' or 'banana pie' in them

    # for each row print if it was apple or banana pie?
    
    # Bonus: Print if the same word appears twice in the same line
    
    # Bonus: has a double character (e.g. 'oo')
    word = re.findall(r"\w*o{2}\w*", lyric)
    print('- has a double character (e.g. \'oo\'):' + str(word))
    print()
search(lyric)
