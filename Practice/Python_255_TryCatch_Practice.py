while True:
    try:
        a = int(input("Tell me one number:"))
        if (a < -1 or a > 10):
            print("Number exceed range, try again")
        elif a in range(1,10): 
            break      
    except:        
        print("Invalid input, only number allow")
print(str(a))