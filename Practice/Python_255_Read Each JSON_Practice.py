def readFile(fileName):
    myFile = None
    try:
        myfile = open(fileName, 'r')     
        return myfile.readlines()
    except IOError:
        print("File is not found")
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file to close")

fileName= "National Internet Using.json"
print(type(readFile(fileName)))
print(readFile(fileName))