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
        return list.copy()
    except IOError:
        print("File is not found")
        return []
    finally:
        if myFile == None:
            print("There is no file to close")
        else:
            myFile.close()
        

fileName= "Test File Multiple Line.txt"
print(type(readFile(fileName)))
newList = readFile(fileName)
newList[len(newList) - 1] = ["Crazy"]
print(newList)
