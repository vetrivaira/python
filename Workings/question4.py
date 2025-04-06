n = int (input())

if(n%2==0):
    
    if (n>=2 and n<=5):
        print ("Not Weired")
        print (n%2)
        
    elif (n>=6 and n<=20):
        print("Weird")
        
    elif (n>20):
        print("Not Weird")
    
else:
    print("Weird")
