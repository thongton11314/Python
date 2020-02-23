# Option 1 - Data Analysis
# Objectives
# 	Understand how to read files using Python
# 	Use list, dictionary, and programming elements to analyze the data from the file
# 	Use Json package to read Json from a file
# 	Use Mathplotlib to draw a scatter plot
# Instruction
# 	Download the data file from the Canvas : https://inst-fs-iad-prod.inscloudgate.net/files/56069e48-8819-4c25-b891-6afd680c68d3/usagov_bitly_data2012-03-16-1331923249.txt?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1ODIzMzA0MTAsInVzZXJfaWQiOiI5MDAwMDAwNDM5NDM2OSIsInJlc291cmNlIjoiL2ZpbGVzLzU2MDY5ZTQ4LTg4MTktNGMyNS1iODkxLTZhZmQ2ODBjNjhkMy91c2Fnb3ZfYml0bHlfZGF0YTIwMTItMDMtMTYtMTMzMTkyMzI0OS50eHQiLCJob3N0IjoiZWRjYy5pbnN0cnVjdHVyZS5jb20iLCJleHAiOjE1ODI0MTY4MTB9.L9PSvttI-kjajMr4uTSGbrnJvrBfTWt-xmPQPCEVbG2vARbDi334p2Q8jYVLi0MjjBUlNOMyDfZmdWCsufGf1w&session_jwt=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImRlZmF1bHQifQ.eyJpZGVudGl0aWVzIjp7ImNhbnZhcyI6eyJ1c2VyX2lkIjoiOTAwMDAwMDQzOTQzNjkiLCJjcmVhdGVkIjoiMjAyMC0wMi0yMlQwNDoyNDowOS40MDFaIn19LCJleHAiOjE1ODIzNDU1NjksImlhdCI6MTU4MjM0NTQ0OX0.H6lxgdu7R8WmSTTA9XWhj842KFw8T5BO6PaQxFIHA1MBVbKCHesAYxWag5mcMv0p7o8VeAsWyEAi_EmDk4KagA
# 	Import json library to read data into a list of records
# 	Use list, dictionary, and programming elements to display 10 ten regions (timezone) that use the Internet
# 	Draw a horizontal bar chart to display the top ten regions and scatter plot of the data.
# Submission
# 	The py source code
# 	Snapshots of the scatter plot and the horizontal bar chart


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


url = "https://inst-fs-iad-prod.inscloudgate.net/files/56069e48-8819-4c25-b891-6afd680c68d3/usagov_bitly_data2012-03-16-1331923249.txt?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1ODI0MzE0NTQsInVzZXJfaWQiOiI5MDAwMDAwNDM5NDM2OSIsInJlc291cmNlIjoiL2ZpbGVzLzU2MDY5ZTQ4LTg4MTktNGMyNS1iODkxLTZhZmQ2ODBjNjhkMy91c2Fnb3ZfYml0bHlfZGF0YTIwMTItMDMtMTYtMTMzMTkyMzI0OS50eHQiLCJob3N0IjoiZWRjYy5pbnN0cnVjdHVyZS5jb20iLCJleHAiOjE1ODI1MTc4NTR9.rvb7SO5oy_V2Z-WYvGj_mS-N6wd3oEHRlZ9H9EvOdlHXiVikJBdrsHIzj1rfNzUYzifRrkEovje2ZkhnurQ_hQ&session_jwt=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImRlZmF1bHQifQ.eyJpZGVudGl0aWVzIjp7ImNhbnZhcyI6eyJ1c2VyX2lkIjoiOTAwMDAwMDQzOTQzNjkiLCJjcmVhdGVkIjoiMjAyMC0wMi0yM1QwODo0MzozMC4xODhaIn19LCJleHAiOjE1ODI0NDc1MzAsImlhdCI6MTU4MjQ0NzQxMH0.VbllYubllzbxSTPFZMioOfc3lrf9Q7AHg5o2YAXSVz1wGRJzoP2PG-IqiVjGIrNXVffwg1_6nnXNtHAgmuO_dA"

import urllib.request as request
import json
with request.urlopen(url) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')