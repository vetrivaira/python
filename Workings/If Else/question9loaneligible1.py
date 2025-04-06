salary = int (input("Enter Your Salary : "))

age = int (input("Enter Your Age : "))

if (salary>=20000 or age<=25):

    loanAmount = int (input("Enter The Loan Amount : "))

    if (loanAmount>=50000):
        
        print("Maximum Loan Amount is Rs.50000/-")
    
    else:

            print ("You Are Eligible for Loan")

else:

    print ("You Are Not Eligible for Loan")
