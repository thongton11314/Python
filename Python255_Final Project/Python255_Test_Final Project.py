import unittest
from collections import Counter


class FinalProject:
    def __init__(self):
        pass

    def removeHeartbeat(self, lst):
        for each in reversed(lst):
            if len(each.keys()) == 1:
                lst.remove(each)

    def countTimeZone(self, lst):
        validTZ = 0 
        nonValidTZ = 0    
        for each in lst:
            if len(each["tz"]) > 0:
                validTZ = validTZ + 1
            else:
                nonValidTZ = nonValidTZ + 1
        return (validTZ, nonValidTZ)

    def dicOfTimeZone(self, lst):
        myDict = {}
        for each in lst:
            if len(each["tz"]) > 0:
                if each["tz"] in myDict:
                    myDict[each["tz"]] += 1
                else:
                    myDict[each["tz"]] = 1
        return myDict

    def topTenTimeZone(self, dic):
        #Count the most commom in dict
        counter = Counter(dic)
        tenCountry = counter.most_common(10)
        return tenCountry



