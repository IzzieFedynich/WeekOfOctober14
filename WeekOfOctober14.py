# Starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSides = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSides * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi



print(archimedes(8))
print(archimedes(16))


for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close

# Modify the Archimedes function to take the radius of the circle as a parameter
# Can you get a better answer more quickly using a larger circle?

# Accumulators
# accumulators are not an equation they are plugging in the acc for the acc and adding it to the x
# gradually

acc = 0
for x in range(1,6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
even_total = 0
for number in range(1, 100 + 1):
    if (number % 2 == 0):
        even_total = even_total + number

print("The Sum of Even Numbers from 1 to 100 = {1}".format(number, even_total))

# compute the sum of the first 50 odd numbers
odd_total = 0
for number in range(1, 50 + 1):
    if (number % 2 == 0):
        odd_total = odd_total + number

print("The Sum of odd Numbers from 1 to 50 = {1}".format(number, odd_total))

# Python Program to find Sum of Even and Odd Numbers from 1 to N



print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, even_total))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, odd_total))

# compute the average of the first 100 odd numbers



# write a function that returns the average of the first N numbers, where
#   N is a parameter

# write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter

# Each number in the Fibonacci sequence is the sum of the previous two numbers

# The first two numbers in the sequence are 1 and. Compute the 10th
# Fibonacci number

print("the fibonacci sequence numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ")

# Write a functions to compute the Nth Fibonacci number, where N is a parameter

# You may assume that N will be greater than or equal to 3

print( )
print( )

# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expresions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == the same as [ equal to ]
# != NOT equal to

dogWeight = 25
print(dogWeight <= 25)
# equals is an assignment equal to is to compare
catWeight = 15

# compound Boolean operators
# snf
# or
# not-false

print( )
print( catWeight < 20)

# Decision Making -- Selection statements
a = 5
b = 10
c = 75

if a <= b:
    c = 45

print(c)


if a > b:
    c = 45
    if b> c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b== a:
        c = 25


print(a, b, c)


d = 85
e = 72
f = 44
ans = 0

if d > e:
    ans= 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)
