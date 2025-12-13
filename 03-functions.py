# PRACTICAL QUESTIONS – FUNCTIONS, ITERATORS, GENERATORS, LAMBDA, MAP & FILTER

# 1. Write a Python function that takes a list of numbers as input and returns
#    the sum of all even numbers present in the list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11]


def evenSum(list):
    sum = 0
    for a in list:
        if a % 2 == 0:
            sum = sum + a
    return sum


print(evenSum(list1))


# 2. Create a Python function that accepts a string as input and returns
#    the reverse of that string.
string = "priyesh"


def revStr(word):
    revString = ""
    for x in range(len(word) - 1):
        revString = word[::-1]
    return revString


print(revStr(string))


# 3. Implement a Python function that takes a list of integers and returns
#    a new list containing the square of each number from the original list.

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sqr(listIn):
    sqrList = []
    for x in listIn:
        sqrList.append(x * x)
    return sqrList


print(sqr(list2))


# 4. Write a Python function that checks whether a given number is prime or not,
#    considering numbers in the range from 1 to 200.
def isPrime(num):
    if num <= 1:
        return "not prime"

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "not prime"

    return "prime"


number = int(input("enter a number (1-200): "))

if number <= 0 or number > 200:
    print("please enter number between 1 - 200")
else:
    print(f"number {number} is {isPrime(number)}")


# 5. Create an iterator class in Python that generates the Fibonacci sequence
#    up to a specified number of terms provided by the user.
def fibo(num):
    a = 0
    b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b


num1 = int(input("Enter number of terms: "))

for value in fibo(num1):
    print(value)

# 6. Write a generator function in Python that yields the powers of 2
#    up to a given exponent.
#
# 7. Implement a generator function that reads a file line by line
#    and yields each line as a string without loading the entire file into memory.
#
# 8. Use a lambda function in Python to sort a list of tuples
#    based on the second element of each tuple.
#
# 9. Write a Python program that uses the `map()` function to convert
#    a list of temperatures from Celsius to Fahrenheit.
#
# 10. Create a Python program that uses the `filter()` function to remove
#     all the vowels from a given string.
#
# 11. Imagine an accounting routine used in a book shop. It works on a list
#     containing sublists with the following data:
#     - Order Number
#     - Book Title and Author
#     - Quantity
#     - Price per Item
#
#     Write a Python program that returns a list of 2-tuples, where each tuple
#     consists of the order number and the product of the price per item
#     and the quantity.
#
#     If the total order value is less than 100.00, increase the product value
#     by 10.00.
#
#     Implement this solution using lambda functions and the `map()` function.
# =====================================================================================
