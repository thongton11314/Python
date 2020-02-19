
def readFile2List(fileName):
    try:
        myFile = open(fileName)
        return myFile.readlines()
    except IOError:
        print('File Not Found', fileName)
        return []
    finally:
        myFile.close()

lst = readFile2List('song.txt')
print(lst)