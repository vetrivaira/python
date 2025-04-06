a = int (input("Enter Number 1 : "))

b = int (input("Enter Number 2 : "))

c = input ("Enter calculation Type (add/sub/mul/div) :")

if (c=="add"):

            print (a,"+",b,"=",a+b)

elif (c=="sub"):

            print (a,"-",b, "=",a-b)

elif (c=="mul"):

            print (a,"x",b, "=",a*b)

elif (c=="div"):

            print (a,"/",b, "=",a/b)

else:

    print ("Please Enter the Correct Calculation Type!!!")
