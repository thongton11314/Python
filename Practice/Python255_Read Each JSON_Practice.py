import json

#Note: Generally speaking, putting more than one JSON object into a file makes that file invalid, broken JSON
def readFile(fileName):
    myFile = None   
    lst = []
    try:
        myFile = open(fileName, 'r')
        while True:
            line = myFile.readline()
            if line.strip():
                lst.append(json.loads(line))
            if not line:
                break
        return lst
    except IOError:
        print("File is not found:" , fileName)
        return []
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file name:", fileName, "to close")
        
fileName= "National Internet Using.json"
lst = readFile(fileName)
