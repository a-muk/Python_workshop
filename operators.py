# arithmetic operators

x = 1
y = 2
z = x+y
print(z)
z = x-y
print(z)
z = x*y
print(z)
z = x/y
print(z)
z = x**y
print(z)
z = x//y
print(z)
z = x % y
print(z)

# assignment
# x=x+1
x += 1
x -= 1
x *= 1
x %= 1
# comparison

# logical operators - or - even if one is true, then the answer is true , and - if both are true, then only the answer is true  , not - negation
print(x > y and x < y)
print(x != y)


# and - In the expression x and y if the first operand (x) is false then return the first operand , else the second

# or - In the expression x or y if the first operand (x) is false then return the second  operand , else the first
print(x and y)
print(x or y)


# identity - is and is not
print(x is y)
print(x is not y)

# membership operators
x = "hello"
y = "h"
print(y in x)
print(x not in y)

# bitwise operators - bitwise |, bitwise & , ^ , << , >> , ~

# type casting
x = 1
y = 1.2
y = '2'
print(x+int(y))

# error
# z = "abc"
# print(x+int(z))
