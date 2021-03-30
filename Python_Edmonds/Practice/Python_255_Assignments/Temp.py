lst = [{"_heartbeat_":1331926831}, {"Data":None}, {"_heartbeat_":1331926831}, {"_heartbeat_":1331926831}]
for each in reversed(lst):
    temp = {"_heartbeat_": None}
    if each.keys() == temp.keys():
        lst.remove(each)
print(lst)