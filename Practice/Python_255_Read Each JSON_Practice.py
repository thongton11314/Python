def readFile(fileName):
    myFile = None   
    list = []
    try:
        myfile = open(fileName, 'r')
        while True:
            line = myfile.readline()
            if line.strip():
                list.append(line.strip())
            if not line:
                break
        return list
    except IOError:
        print("File is not found")
        return []
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file to close")

fileName= "Test File Multiple Line.txt"
print(type(readFile(fileName)))
print(readFile(fileName))