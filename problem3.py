#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
import math
x = input("Please enter a number")
y = input("Please enter another number")
z = input("Please enter another number")
x = int(x)
y = int(y)
z = int(z)
x < y and z
z > y and x
x < y < z
if math.sqrt(x**2 + y**2) == z and y in range(x,z):
    print(x,y,z, "form a Pythagoran triple")
else:
    print(x,y,z, "do not form a Pythagoran triple")
