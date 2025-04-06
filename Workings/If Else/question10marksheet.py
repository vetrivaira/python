tamil = int(input("Tamil : "))
english = int (input("English : "))
maths = int (input("Maths : "))
science = int (input("Science : "))
sscience = int (input("Social Science : "))
total = tamil+english+maths+science+sscience
average = total/5

print("Total = ",total)
print("Average = ",average)

if (average<35):

        print ("Additional Class Required")

else:
        print ("You Are Good to Go")
