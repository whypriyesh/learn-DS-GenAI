# 1 Write a Python program to print "Hello priyesh" on the screen.
print("hello priyeh")

# 2 Write a Python program that displays your name and age on the screen.
name = "priyesh"
age = 11

print(f"hello my name is {name} and I am {age} years old")

# 3 Write code to print all the pre-defined keywords in Python using the keyword library
import keyword

keywords = keyword.kwlist
print(keywords)

# 4 Write a program that checks if a given word is a Python keyword.
word = input("enter ur word: ")

if word in keywords:
    print(f"{word} is a python keyword")
else:
    print(f"{word} is not a python keyword")

# 5 Create a list and tuple in Python, and demonstrate how attempting to change an element works differently for each.

list = ["priyesh", 11, True, 3.14]
tuple = ("priyesh", 12, False, 3.17)

list[0] = "postyesh"  # value changed

# tuple[0] = 'postyesh' # this will give an error as tuple is immutable

# print(list)
# print(tuple)

# 6. Write a function to demonstrate the behavior of mutable and immutable arguments


def mylist(list):
    list[1] = 9
    print(list)


def mytuple(tuple):
    # tuple[1] = 13 #error
    print(tuple)


mylist(list)
mytuple(tuple)


# 7. Write a program that performs basic arithmetic operations on two user-input numbers.

print("welcome to priyesh calculator")
num1 = float(input("enter the number 1: "))
num2 = float(input("enter the number 2: "))

opr = int(
    input(
        """what do u want to do? 
    1-> +
    2-> -
    3-> *
    4-> /
    5-> %
    6-> **
"""
    )
)


def add(x, y):
    print(f"the addition of {x} + {y} is {x+y}")


def subtr(x, y):
    print(f"the subtraction of {x} - {y} is {x-y}")


def multi(x, y):
    print(f"the multiplication of {x} * {y} is {x*y}")


def div(x, y):
    print(f"the division of {x} / {y} is {x/y}")


def mod(x, y):
    print(f"the modulo of {x} % {y} is {x%y}")


def pwr(x, y):
    print(f"the power of {x} ** {y} is {x**y}")


if opr == 1:
    add(num1, num2)

elif opr == 2:
    subtr(num1, num2)

elif opr == 3:
    multi(num1, num2)

elif opr == 4:
    div(num1, num2)

elif opr == 5:
    mod(num1, num2)

else:
    pwr(num1, num2)


# 8. Write a program to demonstrate the use of logical operators.

a = True
b = False
print(f"a and b is {a and b}")
print(f"a or b is {a or b}")
print(f"not a is {not a}")
print(f"not b is {not b}")


# 9. Write a Python program to convert user input from string to integer, float, and boolean types
thing = input("enter something: ")
int_thing = int(thing)
float_thing = float(thing)
bool_thing = bool(thing)
print(f"ur input is int:{int_thing}, float: {float_thing}, boolean: {bool_thing}")


# 10. Write code to demonstrate type casting with list elements.

mylist = ["12", "3.14", "True", "hello"]
int_element = int(mylist[0])
float_element = float(mylist[1])
bool_element = mylist[2] == "True"
str_element = str(mylist[3])
print(
    f"list elements after type casting: int: {int_element}, float: {float_element}, boolean: {bool_element}, string: {str_element}"
)

# 11. Write a program that checks if a number is positive, negative, or zero

num = float(input("enter a number: "))

if num > 0:
    print(f"the number {num} is positive")
elif num < 0:
    print(f"the number {num} is negetive")
else:
    print(f"the number {num} is 0")

# 12. Write a for loop to print numbers from 1 to 10.

for a in range(1, 11):
    print(a)

# 13. Write a Python program to find the sum of all even numbers between 1 and 50

sum = 0
for x in range(1, 51):
    if x % 2 == 0:
        sum += x
    else:
        pass
print(f"the sum of all even numbers between 1 and 50 is {sum}")


# 14. Write a program to reverse a string using a while loop
string = input("enter something: ")
i = len(string) - 1
rev = ""

while i >= 0:
    rev += string[i]
    i -= 1

print(rev)


# 15. Write a Python program to calculate the factorial of a number provided by the user using a while loop
number = int(input("enter a number: "))
if number == 0:
    print("the factorial of 0 is 1")
elif number < 0:
    print("the factorial of negetive number is not defined")
else:

    factorial = 1
    i = 1
    while i <= number:
        factorial = factorial * i
        i = i + 1
    print(f"the factorial of {number} is {factorial}")

# end
