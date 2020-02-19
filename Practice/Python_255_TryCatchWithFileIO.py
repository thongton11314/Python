#This function read all text from a file to a list of string
def readFile2List(fileName):
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
nameOfFile = 'Python_255_TryCatchWithFileIO_Song.txt'
lst = readFile2List(nameOfFile)
print(lst)