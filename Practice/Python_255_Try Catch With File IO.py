#This function read all text from a file to a list of string
def readFileToList(fileName):
    myFile = None
    try:
        myFile = open(fileName)
        return myFile.readlines()
    except IOError:
        print('File Not Found', fileName)
        return []
    finally:
        if myFile is not None:
            myFile.close()

'''
Write a fuction that accepts a list string and performs the following tasks
a. Tokenize and remove all linefeeds
b. Count the freequence of each token using dictionary
'''

def tokenize(lyric):
    result = []
    for item in lyric:
        item = item.replace('\n', '')
        result = result + item.split(' ')
    return result

def countWord(listOfWord):   
    myDict = {}
    for word in listOfWord:
        if word in myDict:
            myDict[word] += myDict[word]
        else:
            myDict[word] = 1
    return myDict

nameOfFile = 'Python_255_TryCatchWithFileIO_Song.txt'
lst = readFileToList(nameOfFile)
listOfWord = tokenize(lst)
print(listOfWord)
print("Most frequency word:" + max(countWord(listOfWord)))
