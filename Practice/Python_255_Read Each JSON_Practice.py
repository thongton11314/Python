def readFile(fileName):
    myFile = None   
    list = []
    try:
        myFile = open(fileName, 'r')
        while True:
            line = myFile.readline()
            if line.strip():
                list.append(line.strip())
            if not line:
                break
        return list.copy()
    except IOError:
        print("File is not found:" , fileName)
        return []
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file name:", fileName, "to close")
        

fileName= "Test File Multiple Line.txt"
print(readFile(fileName))
