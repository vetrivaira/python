#Task
#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

#Example
#Print the following:
#8
#-2
#15

if __name__=='__main__':

    a = int(input())
    b = int(input())

print(f"{a + b}\n{a - b}\n{a * b}")

#The provided code stub reads two integers,  and , from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  a//b .
# The second line should contain the result of float division,  a/b .
#No rounding or formatting is necessary.
#Print:
#0
#0.6

print(f"{a//b}\n{a/b}")