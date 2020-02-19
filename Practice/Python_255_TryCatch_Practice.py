flag = True
while flag is True:
    try:
        a = int(input("Tell me one number:"))
        if (a < -1 or a > 10):
            print("Number exceed range, try again")
            flag = True
        else:
            flag = False        
    except:        
        print("Invalid input, only number allow")
        flag = True
print(str(a))