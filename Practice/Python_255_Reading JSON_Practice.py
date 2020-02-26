import json

#Read only one JSON at a time
def readingFromJSON(fileName):
    myFile = None
    #Open file
    try:
       with open(fileName) as myFile:
           data = json.load(myFile)
       return data
    #Any error relative to files
    except IOError:
        print("File is not found")
    #Close file
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file to close")

#File name
temp = "JSON_Test.txt" 
#Print data to file
print("Test reading from file")
data = readingFromJSON(temp)
data.update({"Thong": 1})
print(type(data))
print(data["Person 1"]["Name"])
print(data["Thong"])