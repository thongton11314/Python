# Practice with nested Dictionary
# Imply JSON library

import json

# This function will write data to txt file
# Input:
#   fileName: the name of the file
#   data: the data from user
# Output:
#   a file has the [fileName.txt] with [data] in it
def writeToJSON(fileName, data):
    myFile = None
    #Open file
    try:
        myFile = open(fileName, 'w')
        json.dump(data, myFile)
    #Any error relative to file
    except IOError:
        print("File is not found") 
    #Close file
    finally:
        if myFile is not None:
            myFile.close()
        else:
            print("There is no file to close")  

# This function will read data to json format
# Input:
#   fileName: the name of the file
# Output:
#   a dictionary filed by data from [filename]
def readingFromJSON(fileName):
    myFile = None
    #Open file
    try:
       myFile = open(fileName) #same as (with open(fileName) as myFile:)
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

#Maked up data
peopleInfor = { 
    "Person 1" : { 
        "Name" : "Thong",
        "Year" : 1995,
        "National" : "Vietnam",
        "Good at" : ["Computer science", "Tennis"]
    },
    "Person 2" : { 
        "Name" : "Thanh",
        "Year" : 1991,
        "National" : "Vietnam",
        "Good at" : ["Hardware", "Dummy things"]
    },
    "Person 3" : { 
        "Name" : "Diep",
        "Year" : 1989,
        "National" : "Vietnam",
        "Good at": ["Enviromental Engineering", "Running"]
    } 
}

#File name
fileName = "JSON_Test.txt"
#Write data to file 
writeToJSON(fileName, peopleInfor)
#Print data to file
print("Test reading from file")
data = readingFromJSON(fileName)
for eachPerson in data:
    print("Name:" + data[eachPerson].get("Name") 
        + " - Year:" + str(data[eachPerson].get("Year")) 
        + " - National:" + data[eachPerson].get("National")
        + " - Good at:" + str(data[eachPerson].get("Good at"))
    )