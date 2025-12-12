# Python Data Structures Exercises

# 1.Write a code to create a string with your name and print it
name = "priyesh"
print(name)

# 2.Write a code to find the length of the string "Hello World"
len("Hello World")
print(f'the length of "hello world" is {len("Hello World")}')

# 3.Write a code to slice the first 3 characters from the string "Python Programming"
string = "Python Programming"
new_string = string[0:3]
print(new_string)

# 4. Write a code to convert the string "hello" to uppercase
str2 = "hello"
print(str2.upper())

# 5.Write a code to replace the word "apple" with "orange" in the string "I like apple"
str3 = "I like apple"
str4 = str3.replace("apple", "orange")
print(str4)

# 6.Write a code to create a list with numbers 1 to 5 and print it
list = []
for x in range(1, 6):
    list.append(x)
print(list)

# 7.Write a code to append the number 10 to the list [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list2.append(10)
print(list2)

# 8. Write a code to remove the number 3 from the list [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 4, 5]
list3.pop(2)
print(list3)

# 9.Write a code to access the second element in the list ['a', 'b', 'c', 'd']
list4 = ["a", "b", "c", "d"]
print(list4[1])

# 10.Write a code to reverse the list [10, 20, 30, 40, 50]
list5 = [10, 20, 30, 40, 50]
list5.reverse()
print(list5)

# 11. Write a code to create a tuple with the elements 100, 200, 300 and print it
tup = (100, 200, 300)
print(tup)

# 12. Write a code to access the second-to-last element of the tuple ('red', 'green', 'blue', 'yellow')
tup2 = ("red", "green", "blue", "yellow")
print(tup2[1:])

# 13. Write a code to find the minimum number in the tuple (10, 20, 5, 15).
tup3 = (10, 20, 5, 15)
print(min(tup3))

# 14. Write a code to find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit').
tup4 = ("dog", "cat", "rabbit")
print(tup4.index("cat"))

# 15. Write a code to create a tuple containing three different fruits and check if "kiwi" is in it.
tup5 = ("apple", "banana", "kiwi")
if "kiwi" in tup5:
    print(f'the tuple {tup5} has "kiwi" in it')
else:
    print("kiwi not found in the tuple")

# 16. Write a code to create a set with the elements 'a', 'b', 'c' and print it
set = {"a", "b", "c"}
print(set)


# 17. Write a code to clear all elements from the set {1, 2, 3, 4, 5}.
set2 = {1, 2, 3, 4, 5}
set2.clear()
print(set2)

# 18. Write a code to remove the element 4 from the set {1, 2, 3, 4}
set3 = {1, 2, 3, 4}
set3.remove(4)
print(set3)

# 19. Write a code to find the union of two sets {1, 2, 3} and {3, 4, 5}
set4 = {1, 2, 3}
set5 = {3, 4, 5}
set5 = set4.union(set5)
print(set5)

# 20. Write a code to find the intersection of two sets {1, 2, 3} and {2, 3, 4}.
set6 = {1, 2, 3}
set7 = {2, 3, 4}
set8 = set6.intersection(set7)
print(set8)

# 21. Write a code to create a dictionary with the keys "name", "age", and "city", and print it.
dic = {"name": "priyesh", "age": 11, "city": "indore"}
print(dic)

# 22. Write a code to add a new key-value pair "country": "USA" to the dictionary {'name': 'John', 'age': 25}
dic2 = {"name": "John", "age": 25}
dic2["country"] = "USA"
print(dic2)

# 23. Write a code to access the value associated with the key "name" in the dictionary {'name': 'Alice', 'age': 30}.
dic3 = {"name": "Alice", "age": 30}
print(dic3["name"])

# 24. Write a code to remove the key "age" from the dictionary {'name': 'Bob', 'age': 22, 'city': 'New York'}
dic4 = {"name": "Bob", "age": 22, "city": "New York"}
dic4.pop("age")
print(dic4)

# 25. Write a code to check if the key "city" exists in the dictionary {'name': 'Alice', 'city': 'Paris'}.
dic5 = {"name": "Alice", "city": "Paris"}
if "city" in dic5:
    print(f'yes "city" exist in {dic5}')
else:
    print("city is not present")

# 26. Write a code to create a list, a tuple, and a dictionary, and print them all
list6 = [
    "priyesh",
    11,
    3.14,
    True,
]
tup6 = ("priyesh", 9, 11.01, False)
dic6 = {"name": "priyesh", "id": 111, "planet": "3453pier"}
print(f"the list is {list6}, the tuple is {tup6}, the dictionary is {dic6}")

# 27. Write a code to create a list of 5 random numbers between 1 and 100, sort it in ascending order, and print the result(replaced)
list7 = []
for x in range(5):
    num = int(input("Enter a number between 1-100: "))
    if num < 1 or num > 100:
        print("Out of range")
        break
    list7.append(num)
if len(list7) == 5:
    list7.sort()
    print("The sorted list is:", list7)

#28. Write a code to create a list with strings and print the element at the third index.
list8 = ["apple", "banana", "cherry", "date", "elderberry"]
print(list8[2])

#29. Write a code to combine two dictionaries into one and print the result
dic7={"name":"priyesh", "age":11,}
dic8= {"city":"indore", "fav-lang":"python"}
dic7.update(dic8)
print(dic7)

#30. Write a code to convert a list of strings into a set
list9 = ["apple", "banana", "apple", "orange", "banana"]
set9 = set(list9)
print(set9)

#end of 02-dataStructure.py