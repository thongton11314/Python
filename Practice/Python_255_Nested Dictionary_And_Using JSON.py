# Practice with nested Dictionary
# Imply JSON library

import json

peopleInfor = { 
    "Person 1" : { 
        "Name" : "Thong",
        "Year" : 1995,
        "National" : "Vietnam",
        "Good at": ["Computer science", "Tennis"]
    },
    "Person 2" : { 
        "Name" : "Thanh",
        "Year" : 1991,
        "National" : "Vietnam",
        "Good at": ["Hardware", "Dummy things"]
    },
    "Person 3" : { 
        "Name" : "Diep",
        "Year" : 1989,
        "National" : "Vietnam",
        "Good at": ["Enviromental Engineering", "Running"]
    } 
}

for eachPerson in peopleInfor:
    print("Name:" + peopleInfor[eachPerson].get("Name") 
        + " - Year:" + str(peopleInfor[eachPerson].get("Year")) 
        + " - National:" + peopleInfor[eachPerson].get("National")
        + " - Good at:" + str(peopleInfor[eachPerson].get("Good at"))
    )
    