import unittest
from collections import Counter


class FinalProject:

    def removeHeartbeat(self, lst):
        for each in reversed(lst):
            temp = {"_heartbeat_": None}
            if each.keys() == temp.keys():
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
        counter = Counter(dic)
        tenCountry = counter.most_common(10)
        return tenCountry


class TestFunction(unittest.TestCase, FinalProject):

    def testRemoveHeartbeat(self):
        lst = [{"_heartbeat_":1331926831}, {"Data":None}, {"_heartbeat_":1331926831}]
        lst1 = [{"Data":None}]
        FinalProject.removeHeartbeat(self, lst)
        self.assertAlmostEqual(lst, lst1)
    
    def testCountingTimeZone(self):
        lst = [{"tz": "America/Denver"}, {"tz": ""}, {"tz": "Europe/Rome"}]
        count = FinalProject.countTimeZone(self, lst)
        self.assertAlmostEqual(count, (2,1))

    def testDicOfTimeZone(self):
        lst = [{"tz": "America/Denver"}, {"tz": ""}, {"tz": "Europe/Rome"}, {"tz": "Europe/Rome"}]
        dic = {"America/Denver": 1, "Europe/Rome": 2}
        dic1 = FinalProject.dicOfTimeZone(self, lst)
        self.assertAlmostEqual(dic, dic1)

    def testTopTenTimeZone(self):
        dic = {"America/Denver": 1, "Europe/Rome": 10}
        top = FinalProject.topTenTimeZone(self, dic)
        self.assertAlmostEqual(top, [("Europe/Rome", 10), ("America/Denver", 1)])

unittest.main()
