# Practice: Thong Ton
# Source: https://www.youtube.com/watch?v=VU60rEXaOXk&t=409s part 1
#         https://www.youtube.com/watch?v=IqF_XGrFbC8 part 4
#         https://www.youtube.com/watch?v=zys2JuGPGvg part 5
#         https://www.youtube.com/watch?v=CmGLLCDfq6k part 6
# Regular expression used to match string pattern
# My biggest fear at the time during learning coding


import re

##########################################################
#Intro 
# 'r' expression, that avoids python's special characters
# r'\n' mean it's is raw string with two character 'n' and '\n' 
# re.search('n', '\n') first item is pattern, second item is string
print(re.search('\n', '\n\n\n\n\n\n\n'))
print(re.search(r'\n', '\n\n'))
#Output: <re.Match object; span=(0, 1), match='\n'>

print(re.search(r'\n', r'\n\n'))
#Output: None
#Explain: Because string is not new line, but pattern is looking for new line, r'\n\n' ignore new line

##########################################################
#Character set
#Each \w represent for one character
print("L1:" + str(re.search('abcd', 'abcdedfsds abfabcd')))
#Output: <re.Match object; span=(0, 4), match='abcd'>

print("L2:" + str(re.search(r'\w\w\w\w', "abcdefnc abcd"))) #Mathces characters and numbers, alpha numeric character \w matches alpha numeric character [a-zA-Z0-9_]
#Output: <re.Match object; span=(0, 4), match='abcd'>

print("L3:" + str(re.search(r'\w\w\w', "ab_cdefnc abcd")))
#Output: <re.Match object; span=(0, 3), match='ab_'>

print("L4:" + str(re.search(r'\w\w\w\w', "a33-_!")))
#Output: None
#Explain: Beause \w does not include special character, here is '-'

print("L5:" + str(re.search(r'\w\w\w\W\W', "a33- _!")))
#Output: <re.Match object; span=(0, 4), match='a33-'>
#Explain" \W is opposite of \w which mean include special character, this time include '-' and empty space as well

#############################################################
#Quantifiers
#Make code more consice
# + represent 1 or more
# ? represent 0 or 1
# * represent 0 or more
# {start, end} represent range or repetitions, can also work {min,} {,max}
print("L6:" + str(re.search(r'\w+', "abcdefnc abcd")))
#Output: <re.Match object; span=(0, 8), match='abcdefnc'> 
#Explain: \w+ present one or more after the first character of the world until it hit the space

##############################################################
#Group
#Use group to actually print out the world from span index range
print("L7:" + re.search(r'\w+', "FirstWord SecondWord").group())
#Output: FirstWord
#Explain: becuase here I use group() function in class re to print out the word

print("L8:" + re.search(r'\w+\W+\w+', "FirstWord         SecondWord").group())
#Output: FirstWord         SecondWord
#Explain: First, I use there \w+ \W+ \w+ represent for 3 word, I use \W+ at the middle becuase for space. 
#         Second, they are default group up at 0, and group() will execute \w+\W+\w+ as one group

print("L8:" + re.search(r'\w+\w+\w+\w+\w+', "FirstWord SecondWord").group())
#Output: FirstWord SecondWord
#Explain: We can see that ouput only two word but we have many \w+, it is ok. We can write as many as we want

print("L9:" + re.search(r'\w+\W?\w+', "FirstWordSecondWord").group())
print("L10:" + re.search(r'\w+\W?\w+', "FirstWord SecondWord").group())
#Output: FirstWordSecondWord
#        FirstWord SecondWord
#Explain: ? present 0 or 1 instance, so it does not matter that we have special case or not, if we have then \W? will show it, otherwise it will ignore

print("L11:" + re.search(r'\w{3}', "FirstWordSecondWord").group())
#Output: Fir
#Explain: Range maximum letter is 3 letters.

print("L12:" + re.search(r'\w{1,9}', "FirstWordSecondWord").group())
#Output: FirstWord
#Explain: Range from 1 to 9, however index 0-8 

print("L13:" + re.search(r'\w{1,10}\W{0,1}\w+', "FirstWord SecondWord").group()) #First word, max 10 characer. Second word max 1 special case. Third word is entire word
print("L14:" + re.search(r'\w{1,10}\W{0,1}\w+', "FirstWord    SecondWord").group())
#Output: FirstWord SecondWord
#        FirstWord
#Explain: The second result, because it does not match the special character 'space' that exceed than 1 in max range

print("L15:" + re.search(r'\w{0,}\W{0,}\w+', "FirstWord    SecondWord").group()) #First word letter from 0 - ended letter, Second word is 0 to ended special character, Thir word is entire word
print("L15:" + str(re.findall(r'\w{0,}\W{0,}\w+', "FirstWord    SecondWord")))

#Output: FirstWord    SecondWord
#Explain: We set for max range

##############################################################
#Other types of character sets
# \d matches digits [0-9]
# \D matches this matches any non-digit character; ~\d
# \s matches any whitespace character
# \S matches any non-whitespace character ~\s
# . Accept any characters except new line
# ^ Anything that is not

string = '123Word++'
print("L16:" + re.search(r'\d+', string).group())
#Output: 123
#Explain:Print out only number in word because I use \d+

string = '123Word++ 321Word++ 213 Word +++'
print("L17:" + re.search(r'\S+', string).group()) #Matches any  non-white space
string = '123Word++'
print("L18:" + re.search(r'\S+', string).group())
#Ouput: 123Word++

#########################################################################
#Findall function
string = """
I guess we could discuss the implications of the phrase "meant to be." 

That is if we wanted to drown ourselves in a sea of backwardly referential semantics and other mumbo-jumbo. 
"""
print("L19:" + str(re.findall(r'\s+', string))) #Match with bunch of space
#Ouput: a bunc of \n and space
#Explain: Because we use \s+ that match all space and new line

print("L20:" + str(re.findall(r'\S+', string))) #Match with all world that not include white space and new line
#Output: A list of word that seperated from the long string
#        ['I', 'guess', 'we', 'could', 'discuss', 'the', ......]
#Explain: Because we use \S+ that match with world in string only

#We can also use join method to connect each word from the list become a paragraph
print("L21:" + ' '.join(re.findall(r'\S+', string)))
#Output: "I guess we could discuss the implications....... and other mumbo-jumbo"
#Explain: use the build in function to connect each word

print("L22:" + re.search(r'.+', string).group()) # . Accept any characters except new line
#Output: "I guess we could discuss the implications of the phrase "meant to be.""
#Explain: The dot '.' will help to terminate the newline, but we have to use .+ to count up all world before hit the newline

print("L23:" + re.search(r'.+', string, flags = re.DOTALL).group()) #Use the flag to include all newline
#Ouput: The entire string
#Explain: Because I use the flags to tell it include all newline by re.DOTALL

###################################################################################################
#Creating my own character sets
#[] is a metacharacter when use in [] custom character sets, anthing in bracket is custom set

string = "Hello, There, How, Are, Your......."
print("L24:" + str(re.findall(r'[A-Z]',string)))
#Ouput: ['H', 'T', 'H', 'A', 'Y']
#Explain: Because I but the custom word set from A to Z in []

print("L25:" + str(re.findall(r'[A-Z,]',string)))
#Output: ['H', ',', 'T', ',', 'H', ',', 'A', ',', 'Y']
#Explain: Because I but the custom word set from A to Z and comma ',' in []

print("L26:" + str(re.findall(r'[A-Z,.]',string)))
#Ouput: ['H', ',', 'T', ',', 'H', ',', 'A', ',', 'Y', '.', '.', '.', '.', '.', '.', '.']
#Explain: Because I but the custom word set from A to Z and comma ',' and dot '.' in []

print("L27:" + str(re.findall(r'[A-Z,.\s]',string))) #Pull out whole string
#Output: ['H', ',', ' ', 'T', ',', ' ', 'H', ',', ' ', 'A', ',', ' ', 'Y', '.', '.', '.', '.', '.', '.', '.']
#Explain: Because I but the custom word set from A to Z and comma ',', dot '.', and white space \s in []

###########################################################################
#Quantifiers with custom sets

string = "HELLO, Hello, hello, hi, There, How, Are, You..."
print("L28:" + re.search(r'[A-Z]+', string).group())
#Ouput: HELLO

print("L29:" + str(re.findall(r'[A-Z]+',string)))
#Ouput: ['HELLO', 'H', 'T', 'H', 'A', 'Y']
#Explain: Because I print out all of the capital letter in string

print("L30:" + str(re.findall(r'\w[A-Z]+', string)))
#Output: ['HELLO']
#Explain: Because i use \w and range to print out word with ALL CAPITAl

print("L31:" + str(re.findall(r'[A-Za-z\s,.]+',string)))
#Output: ['HELLO, Hello, hello, hi, There, How, Are, You...']
#Explain: When I use find all to find all word that match [A-Za-z\s,.]+ condition

print("L32:" + str(re.findall(r'[A-Z]?[a-z\s,]+', string)))
#Output: ['O, ', 'Hello, hello, hi, ', 'There, ', 'How, ', 'Are, ', 'You']
#Explain: Because ? is condition either has or not for first character

print("L33:" + str(re.findall(r'[^A-Z]+', string)))
#Output: [', ', 'ello, hello, hi, ', 'here, ', 'ow, ', 're, ', 'ou...']
#Explain: Because I print out any character that is not from A-Z

print("L34:" + str(re.findall(r'[^A-Z.,\s]+',string)))
#Output: ['ello', 'hello', 'hi', 'here', 'ow', 're', 'ou']

print("L35:" + str(re.findall(r'\w[^A-Z,.]+', string)))
print("L36:" + str(re.findall(r'\w[a-z]+', string)))
#Output: ['Hello', 'hello', 'hi', 'There', 'How', 'Are', 'You']
#Explain: Because I print out any world that is not ALL CAPITAL

print("L37:" + str(re.findall(r'[Hh][e][l][l][o]+', string)))
#Ouput: ['Hello', 'hello']
#Explain: I set each character with specific letter

print("L38:" + str(re.findall(r'[a-z]', string)))
print("L39:" + str(re.findall(r'[^A-Z\W]', string)))
#Ouput: ['e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o', 'h', 'i', 'h', 'e', 'r', 'e', 'o', 'w', 'r', 'e', 'o', 'u']
#Explain: I set each first character is not capitial and not special letter

#########################################################
#Intro to group
#Group allow us to pull out sections of a match and store them
#Use brackets denotes a group
#() metacharacter
# Using findall does not specify the group function, use search instead to get index of group

string = 'FirstA has 6 cats but I think SecondB has 3 dogs and ThirdC has 5 fishes'
print("LG 1:" + str(re.findall(r'[A-Za-z]+ \w+ \d+ \w+', string)))
#Output: ['FirstA has 6 cats', 'SecondB has 3 dogs', 'ThirdC has 5 fishes']
#Explain: Because [A-Za-z]+ \w+ \d+ \w+ which mean [Word] [word] [number] [word] 

print("LG 2:" + str(re.findall(r'([A-Za-z]+) \w+ \d+ \w+', string)))
#Output: ['A', 'B', 'C']
#Explain: Because ([A-Za-z]) denote a group of name

print("LG 3:" + str(re.findall(r'[A-Za-z]+ \w+ \d+ (\w+)', string)))
#Output: ['cats', 'dogs', 'fishes']
#Explain: Because (\w+) denote a group of animal

print("LG 4:" + str(re.findall(r'([A-Za-z]+) \w+ (\d+) (\w+)', string)))
#Ouput: [('FirstA', '6', 'cats'), ('SecondB', '3', 'dogs'), ('ThirdC', '5', 'fishes')]
#Explain: Because I group ([A-Za-z]+) for name, (\d+) amount, (\w+) animal

match = re.search(r'([A-Za-z]+) \w+ (\d+) (\w+)',string).group()
print(match)
#Output: FirstA has 6 cats
#Explain: It has all group





