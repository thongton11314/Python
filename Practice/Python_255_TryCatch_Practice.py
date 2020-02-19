def getNumber():
    while True:
        try:
            a = int(input("Tell me one number:"))
            if (a < -1 or a > 10):
                print("Number exceed range(1,10), try again")
            elif a in range(1,10): 
                return a     
        except ValueError: #Specific type of eroor, the interpreter will notice ValueError when it occur       
            print("Invalid input, only number allow")
        except: #Anytype of error, the intepreter won't tell the user
            print("Something wrong happened, try again")
print("Number enter:" + str(getNumber()))
