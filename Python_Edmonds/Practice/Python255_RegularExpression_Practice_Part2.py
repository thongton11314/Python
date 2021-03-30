import re

#Start with Ton(^Ton) and keep reading word until(.+) end with Thong (Thong$)
txt = "Ton That Quynh Thong"
x = re.search(r"^Ton.*Thong$", txt) 
print("Test 1:" + x.group())
#Output:Test 1:Ton That Quynh Thong


#Check if the world contains "a" followed by exactly two "l" characters:
txt = "The rain in Spain falls mainly in the plain, but is is called falling fall!"
x = re.findall(r"\w*al{2}\w*", txt)
print("Test 2:" + str(x))
#Output:Test 2:['falls', 'called', 'falling', 'fall']

#Find all digit characters:
txt = "That will be 59 dollars"
x = re.findall(r"\d+", txt)
print("Test 3:" + str(x))
#Output:Test 3:['59']

#Find all not digit characters:
txt = "That will be 59 dollars"
x = re.findall(r"\D[a-z]\w+", txt)
print("Test 4:" + str(x))
#Output:Test 4:['That', ' will', ' be', ' dollars']  

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
txt = "hello world"
x = re.findall(r"he..o", txt)
print("Test 5:" + str(x))
#Output:Test 5:['hello']

#Check if the word contains "ai" followed by 0 or more "x" characters:
txt = "The rain in Spain falls mainly in the plain plaing!"
x = re.findall(r"\w*aix*\w*", txt)
print("Test 6:" + str(x))
#Output:Test 6:['rain', 'Spain', 'mainly', 'plain', 'plaing']

#Check if the word contains "ai" followed by 1 or more "x" characters:
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall(r"aix+", txt)
print("Test 7:" + str(x))
#Output:Test 7:[]

#Check if the string contains either "falls" or "stays":
txt = "The rain in Spain falls mainly in the plain, fall stays stay!"
x = re.findall(r"falls|stays", txt)
print("Test 8:" + str(x))
#Output:Test 8:['falls', 'stays']

#Check if the string starts with "The":
txt = "The rain in Spain"
x = re.findall(r"\AThe", txt)
print("Test 9:" + str(x))
#Output:Test 9:['The']

#Check if "ain" is present at the beginning of a WORD:
txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
print("Test 10:" + str(x))
#Output:Test 10:[]

#Check if "ain" is present at the end of a WORD:
txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
print("Test 11:" + str(x))
#Output:Test 11:['ain', 'ain']

#Print out the word that first letter is not capital
txt = "CAPITALALL notcapitall Firstcapital SomECapiTal cAPITALREST"
x = re.findall(r"\b[a-z]\w+", txt)
print("Test 12:" + str(x))
#Output:Test 12:['notcapitall', 'cAPITALREST']

#Check if "ain" is present, but NOT at the beginning of a word:
txt = "The rain in Spain, painting "
x = re.findall(r"\w*\Bain\w*", txt)
print("Test 13:" + str(x))
#Ouput:Test 13:['rain', 'Spain', 'painting']

#Check if "ain" is present, but NOT at the end of a word:
txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
print("Test 14:" + str(x))
#Output:Test 14:[]

#Return a match at every white-space character:
txt = "The rain in Spain"
x = re.findall(r"\s", txt)
print("Test 15:" + str(x))
#Output:Test 15:[' ', ' ', ' ']

#Return a match at every NON white-space character:
txt = "The rain in Spain"
x = re.findall(r"\S", txt)
print("Test 16:" + str(x))
#Output:Test 16:['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
txt = "The rain in Spain"
x = re.findall(r"\w", txt)
print("Test 17:" + str(x))
#Output:Test 17:['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
txt = "The rain in Spain"
x = re.findall(r"\W", txt)
print("Test 18:" + str(x))
#Output:Test 18:[' ', ' ', ' ']

#Check if the string ends with "Spain":
txt = "The rain in Spain"
x = re.findall(r"Spain\Z", txt)
print("Test 19:" + str(x))
#Output:Test 19:['Spain']

#Check if the string has any a, r, or n characters:
txt = "The rain in Spain"
x = re.findall(r"[arn]", txt)
print("Test 20:" + str(x))
#Output:Test 20:['r', 'a', 'n', 'n', 'a', 'n']

#Check if the string has any characters between a and n:
txt = "The rain in Spain"
x = re.findall(r"[a-n]", txt)
print("Test 21:" + str(x))
#Outpu:Test 21:['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']

#Check if the string has other characters than a, r, or n:
txt = "The rain in Spain"
x = re.findall(r"[^arn]", txt)
print("Test 22:" + str(x))
#Output:Test 22:['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']

#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split(r"\s", txt)
print("Test 23:" + str(x))
#Output:Test 23:['The', 'rain', 'in', 'Spain']

#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split(r"\s", txt, 1)
print("Test 24:" + str(x))
#Output:Test 24:['The', 'rain in Spain']

#Replace all white-space characters with the dash:
txt = "The rain in Spain"
x = re.sub(r"\s", "-", txt)
print("Test 25:" + str(x))
#Output:Test 25:The-rain-in-Spain

#Replace the first two occurrences of a white-space character with the dash:
txt = "The rain in Spain"
x = re.sub(r"\s", "_", txt, 2)
print("Test 26:" + str(x))
#Output:Test 26:The_rain_in Spain

txt = """The rain in Spain (aaa)
assadsadsadas asd asds up on dddsd dddd Bar baz bath bating ?? Thong. """
x = re.findall(r'\w.+', txt)
print("Test 22:" + str(x))


