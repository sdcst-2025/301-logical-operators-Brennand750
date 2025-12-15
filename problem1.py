#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

num = input("Please enter an number")
num = int(num)
if num/6 == int(num/6) and num/8 == int(num/8):
    print("The number is not true")
elif num/6 == int(num/6):
    print("The number is true")
elif num/8 == int(num/8):
    print("The number is true")