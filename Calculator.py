a = int (input("Input Number 1 = "))
b = int (input("Input Number 2 = "))
c = input("Give Input Add/Mul/Sub/Div/Percentage = ")

if c == "Add":

    print("Add Value is  = ",a+b)

elif c == "Mul":

    print ("Multiplication Value is = ",a*b)

elif c == "Sub":

    print ("Subtraction Value is = ",a-b)

elif c == "Div":

    print ("Division Value is = ",a/b)

elif c == "Percentage":

    print ("Percentage is = ", a/b*100)

else:

    print ("Invalid Input")
