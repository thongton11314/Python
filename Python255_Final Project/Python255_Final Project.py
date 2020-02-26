# Option 1 - Data Analysis
# Objectives
# 	Understand how to read files using Python
# 	Use list, dictionary, and programming elements to analyze the data from the file
# 	Use Json package to read Json from a file
# 	Use Mathplotlib to draw a scatter plot
# Instruction
# 	Import json library to read data into a list of records
# 	Use list, dictionary, and programming elements to display 10 ten regions (timezone) that use the Internet
# 	Draw a horizontal bar chart to display the top ten regions and scatter plot of the data.
# Submission
# 	The py source code
# 	Snapshots of the scatter plot and the horizontal bar chart

import json
import collections

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

#Remove some necessray data, heartbeat in particular 
def removeHeartbeat(lst):
    for each in reversed(lst):
        if len(each.keys()) == 1:
            lst.remove(each)

#Return a tubple that first parameter is number of valid time zone, 
# second parameter is number of non-time zone
#Input: list of data
#Output: tubple
def countTimeZone(lst):
    validTZ = 0 
    nonValidTZ = 0    
    for each in lst:
        if len(each["tz"]) > 0:
            validTZ = validTZ + 1
        else:
            nonValidTZ = nonValidTZ + 1
    return (validTZ, nonValidTZ)

def dicOfCountryUsingIntenet(lst):
    #Create a dictionary with [key] = country, value = count up many time appear
    myDict = {}
    for each in lst:
        if len(each["tz"]) > 0:
            if each["tz"] in myDict:
                myDict[each["tz"]] += 1
            else:
                myDict[each["tz"]] = 1
    return myDict

def topTenOfCountryUsingInternet(dic):
    #Sort the dictionary
    print(dic.values())
    #Return the first ten 
    return None

fileName= "National Internet Using.json"
lst = readFile(fileName)
removeHeartbeat(lst)
dicOfContry = dicOfCountryUsingIntenet(lst)
print(len(lst))
print("Valid time-zone and invalid time-zone", countTimeZone(lst))
print(topTenOfCountryUsingInternet(dicOfContry))


