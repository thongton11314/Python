# Practice with nested Dictionary
peopleInfor = { 
    "Person 1" : { 
        "Name" : "Thong",
        "Year" : 1995,
        "National" : "Vietnam"
    },
    "Person 2" : { 
        "Name" : "Thanh",
        "Year" : 1991,
        "National" : "Vietnam"
    },
    "Person 3" : { 
        "Name" : "Diep",
        "Year" : 1989,
        "National" : "Vietnam"
    } 
}

for eachPerson in peopleInfor:
    print(peopleInfor[eachPerson].get("Name") + " " + str(peopleInfor[eachPerson].get("Year")) + " " + peopleInfor[eachPerson].get("National"))