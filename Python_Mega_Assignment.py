# PYTHON MEGA ASSIGNMENT
print("I have added new line")
# Q1. Why do we call Python as a general purpose and high-level programming language?
# Ans:  Python is general purpose programming language because it is used to solve a wide variety of problems. Example – AI, ML, BIG DATA, WEB DEV and many more
# It is high-level programming language because it usages natural languages which is easily understandable 
# by human and it is usages mathematical notations which makes solution easy to understand by human beings.

# Q2. Why is Python called a dynamically typed language?
# ANS: In Python Type check of variable takes place at run time not at declaration time so that execution become faster thats why 
#Python is called as dynamically typed language

# Q3. List some pros and cons of Python programming language?
# ANS: Pros of Python programming language
# 1.Easy to learn and read                        2.Python Enhance productivity 
# 3.Python has vast collection of library         4.Python is free, open-source, and has a vibrant community  
# 5.Python is a portable programming language     6.Python is an interpreted programming language

# Cons of Python programming language
# 1.Python has speed limitations 
# 2.Python is not so strong with mobile computing 
# 3.Python can have runtime errors # 
# 4.Python consumes a lots of memory space 
# 5.Python is not easy to test

# Q4. In what all domains can we use Python?
# ANS: Python has a library either standard or third party for every thing, so technically you could say it's used for everything.
#• Machine learning / Artificial intelligence • Desktop GUI • Data analytics and data visualization • Web development • Game development • Mobile app development • Embedded systems …

# Q5. What are variable and how can we declare them?
# ANS: Variables are the name of memory allocated to store some values in python we can directly declare variable like a=10,a=5.55,a=True
# A Python variable is a symbolic name which reference or point an object In other way Python variable reserved memory location to store values.
# Python has no command for declaring a variable. A variable is created when some value is assigned to it.

# Q6. How can we take an input from the user in Python?
# Ans: We take input from user by simply using input function in our programme. We can also show message to user. It always take input as an string.

# Q7. What is the default datatype of the value that has been taken as an input using input() function?
# ANS:  Default data type of input() method is string.

# Q8. What is type casting?
# ANS: Converting one data-type into another data-type is called type casting.

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
# ANS: Yes, we can take multiple input using input() by requesting user to enter delimited separated field. And then by using .split() method to separate delimited field.

# Q10. What are keywords?
# ANS: Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier. There are 33 keywords in python.

# Q11. Can we use keywords as a variable? Support your answer with reason.
# Ans: Python keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes.

# Q12. What is indentation? What's the use of indentaion in Python?
# ANS: Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only. 
# Python uses indentation to indicate a block of code.

# Q13. How can we throw some output in Python?
# By using print() function, Whatever inside parentheses will be printed on output of the console.

# Q14. What are operators in Python?
# ANS: In Python, operators are special symbols that designate that some sort of computation should be performed. 
# The values that an operator acts on are called operands.

# Q15. What is difference between / and // operators?
# ANS: ‘/’ is a division operator used to divide two integers and gives float data type While ‘//’ is a floor division operator which divide two integers 
# and gives int data-type it simply removes after decimal part.

# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
# ```
# Code: 
a= 'iNeuron'
print(a*4)


# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
# Code: 
num= int(input("Enter a number to check whether it is even or odd  : "))
if num%2==0:
    print(num,"is Even")
else:
    print(num,"is Odd")


# Q18. What are boolean operator?
# ANS: Boolean Operators is the type of operator which is  True and False these operators are used to check the conditions


# Q19. What will the output of the following?
# ```
# 1 or 0
# 0 and 0
# Ans: output for 1 or 0 will be 1
#     output for 0 and 0 will be 0

# True and False and True
#output will be False

# 1 or 0 or 0
# output will be 0



# Q20. What are conditional statements in Python?
# Conditional statements are used in program while making decisions based on the conditions encountered by the program.
# Python has 3 key Conditional Statements
# I. If statement
# II. If else statement
# III. If elif ... elif else 


# Q21. What is use of 'if', 'elif' and 'else' keywords?
#ANS: 
# I. If is used to check the condition in program. If block executed only if condition is true
# II. If else statement -> if block executed if the condition is true Otherwise else block get executed for sure.
# III. If elif else -> One block from if or elif get executed if condition is true otherwise else block will get executed.



# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age=int(input("Enter your age: "))
if age>=18:
    print("I can vote")
else:
    print("I can't vote")


# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
numbers = [12, 75, 150, 180, 145, 525, 50]
sum=0
for i in numbers:
    if i%2==0:
        sum=sum+i
print("The sum of all even numbers is : ",sum)


# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# ANS: 
a=int(input("Enter first Nnumber : "))
b=int(input("Enter second Nnumber : "))
c=int(input("Enter third Nnumber : "))
if a>b and a>c:
    print(a," is the greatest number")
elif b>a and b>c:
    print(b," is the greatest number")
else:
    print(c," is the greatest number")


# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```

# - The number must be divisible by five
numbers = [12, 75, 150, 180, 145, 525, 50]
l=[]
for i in numbers:
    if i%5==0:
        l.append(i)

print(l)


# - If the number is greater than 150, then skip it and move to the next number
numbers = [12, 75, 150, 180, 145, 525, 50]
l=[]
for i in numbers:
    if i>150:
        continue
    l.append(i)
print(l)


# - If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
l=[]
for i in numbers:
    if i>500:
        break
    l.append(i)
print(l)



# Q26. What is a string? How can we declare string in Python?
# ANS: String is collection of charactors. In Python it is a immutable data type.

# We can declare string in python by enclosing characters into single\double quotes, using triple quotes(""" """) 
# we declare doc string, and also by using str() method.
# example 
a='iNeuron'
b="iNeuron Platform" 
c=''' This is 
multiline
string '''


# Q27. How can we access the string using its index?
# ANS: We can access the characters in a string by referring to its index number inside square brackets [] .
# for example 
a='iNeuron'
print(a[1])


# Q28. Write a code to get the desired output of the following
# string = "Big Data iNeuron"
# desired_output = "iNeuron"
str="Big Data iNeuron"
print(str[9:])


# Q29. Write a code to get the desired output of the following
# string = "Big Data iNeuron"
# desired_output = "norueNi"
# CODE:
string = "Big Data iNeuron"
print(string[:-8:-1])


# Q30. Resverse the string given in the above question.
# CODE:
string = "Big Data iNeuron"
print(string[::-1])


# Q31. How can you delete entire string at once?
# CODE:
a= 'String'
del a #the del keyword will delete the string a


# Q32. What is escape sequence?
# ANS: An escape sequence is a sequence of characters that does not represent itself when used inside a character
# or string literal, but is translated into another character or a sequence of characters that may be difficult or
# impossible to represent directly.
# Example :-
#     \a,  \t,   \n,   \\,    \r   . . . 



# Q33. How can you print the below string?
# 'iNeuron's Big Data Course'
s = "\'iNeuron\'s Big Data Course\'"
for i in s:
    print(i, end='')


# Q34. What is a list in Python?
# Ans: list a predefined data structure in python which can hold values of different data types and list is mutable
# We create Python list by placing elements inside square brackets [] , separated by commas.


# Q35. How can you create a list in Python?
# ANS:  By simply placing elements\Object`s inside square brackets [], separated by comma.
#  example first_list= [] this is empty list


# Q36. How can we access the elements in a list?
# ANS: To access elements from list we can use index method by placing index inside [index].
# Or we can use string sclicing method [start:stop:step].


# Q37. Write a code to access the word "iNeuron" from the given list.
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])


# Q38. Take a list as an input from the user and find the length of the list.
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)
print("The length of the list is : ",len(lst))



# Q39. Add the word "Big" in the 3rd index of the given list.
lst = ["Welcome", "to", "Data", "course"]
lst.insert(3,'Big')
print(lst)


# Q40. What is a tuple? How is it different from list?
# ANS: Tuple is a predefined data structure im python which is immutable
# Tuple is collection of ordered, unchangeable items that allow duplicate values.
# In list we can modify items but touple isn`t allow to modify items in it. That means touple is immutable.
#Tuple is fast and need less memory while list is slow and need more memory


# Q41. How can you create a tuple in Python?
# ANS: A tuple is created by placing all the items (elements) inside parentheses () , separated by commas.


# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
# ANS: 
t = ()
type(t)
t.append("Furquan")
# it will give error we can not do adding/updating/appending items/elements because the tuple is immutable 


# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
# ANS:
# Yes
t1 = (1,1.234,1+2j)
t2 = ('a','b','c',True,False)
t = t1 + t2
print(t)
# + operation first unpack elements and then add, that`s why it is possible.


# Q44. Take a tuple as an input and print the count of elements in it.
# ANS: 
flag = True
while flag:
    try:
        a = eval(input("Enter a tuple :"))
        if type(a) == tuple:
            flag = False
        else:
            raise Exception("Not a tuple")
    except Exception as e:
        print("Wrong input :", e) 
print("The length of",a,"is :",len(a))
# The length of (1, 2) is : 2



# Q45. What are sets in Python?
# ANS: set is a predefined data structure in python
# set does not conatin duplicate values it is unordered an unindexed


# Q46. How can you create a set?
# By using { } brackets we can create set
# example :
set1= set() # if the set is emmpty then () brackets are required to create it
print(type(set1))


# Q47. Create a set and add "iNeuron" in your set.
set1= set()
set1.add('iNeuron')
print(set1)



# Q48. Try to add multiple values using add() function.
s = set()
s.add(("iNeuron","is","best")) # add() only add single values. else it will consider as tuple
print(s)


# Q49. How is update() different from add()?
# ANS:
# We use add() method to add single value to a set.
# We use update() method to add sequence values to a set.


# Q50. What is clear() in sets?
# ANS: The clear() method removes all elements in a set.


# Q51. What is frozen set?
# ANS: Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time,
# elements of the frozen set remain the same after creation.


# Q52. How is frozen set different from set?
# ANS: Once generated elements from the frozenset cannot be added or removed while in set it is possible.


# Q53. What is union() in sets? Explain via code.
# ANS:
# Union in set combine all the elements from both the sets, Ex {1,2,3} U {7,8,9} = {1,2,3,7,8,9}
# Let,
a = {1,2,3}
b = {7,8,9}
c = a.union(b) # c is union of a and b
print(c)


# Q54. What is intersection() in sets? Explain via code.
# ANS:
# intersection in set remove all the common elements from both the sets, Ex {1,2,3} ∩ {7,8,9} = {}
# Let,
a = {1,2,3,11,12}
b = {7,8,11,9,12}
c = a.intersection(b) # c is intersection of a and b, only common elements will store in python
print(c)


# Q55. What is dictionary in Python?
# ANS:
# Dictionary is predefined datastructure in python
# Dictionary store its elements in key value pair.
# A dictionary is an unordered and mutable Python container that stores mappings of unique keys to values.


# Q56. How is dictionary different from all other data structures.
# ANS:
# A dictionary objects are stored in key value formates, Dictionary values are accessed using its key,
# while Other data structures are stored in containers format and its value are accessed through index method.


# Q57. How can we delare a dictionary in Python?
# ANS:
# Using {}, in which key:values are defined and by dict() method we declare dictionary in python.


# Q58. What will the output of the following?
var = {}
print(type(var))
# ANS: <class 'dict'>


# Q59. How can we add an element in a dictionary?
# ANS:
# In front of dict name, by writting keys within square brackets [] and then assign the value to it.
# Dict_name["keys"] = 'Values'


# Q60. Create a dictionary and access all the values in that dictionary.
# ANS:
my_dict = {1:"iNeuron", 2:"is", 3:"best", 4:"platform !!!"}
print(my_dict[1], my_dict[2], my_dict[3], my_dict[4])


# Q61. Create a nested dictionary and access all the element in the inner dictionary.
# ANS: 
d = {1:{1,2,3,4}, 2:{5,6,7,8}, 3:{9,10}}
for item in d:
    for val in d[item]:
        print(val)
print(d.get(1))


# Q62. What is the use of get() function?
# ANS:
#     Return the value for key if key is in the dictionary, else None.
d = {1:{1,2,3,4}, 2:{5,6,7,8}, 3:{9,10}}
print(d.get(1))



# Q63. What is the use of items() function?
# ANS:
#  A set-like object providing a view on Dictionary items, every key value pairs are represented as set.
d = {1:{1,2,3,4}, 2:{5,6,7,8}, 3:{9,10}}
print(d.items())


# Q64. What is the use of pop() function?
# ANS:
# It remove the items at specific position
d = [1,2.3,3,56]
d.pop(0)
print(d)


# Q65. What is the use of popitems() function?
# ANS:
# The popitem() method removes the item that was last inserted into the dictionary.
d = {1:{1,2,3,4}, 2:{5,6,7,8}, 3:{9,10}}
d.popitem()
print(d)


# Q66. What is the use of keys() function?
# ANS:
# It gives view of dictionary keys in set like like formate.
d = {1:{1,2,3,4}, 2:{5,6,7,8}, 3:{9,10}}
print(d.keys())



# Q67. What is the use of values() function?
# ANS:
# It gives view of dictionary values in set like like formate.
d = {1:{1,2,3,4}, 2:{5,6,7,8}, 3:{9,10}}
print(d.values())


# Q68. What are loops in Python?
# ANS:
# Loops in python used to loop through certain peace of code while conditions are  not matched.



# Q69. How many type of loop are there in Python?
# ANS:
# There are two types of loops in python for loop and while loop


# Q70. What is the difference between for and while loops?
# ANS:
# for loop :- try to iterate over certain no of times, each time conditions are not checked.
# while loop :- first check the conditions then executes code, no of executions are not predefined.


# Q71. What is the use of continue statement?
# ANS:
# A continue statement ends the current iteration of a loop.
# Program control is passed from the continue statement to the end of the loop body.
# if the conditon is true then then control skips the iteration and check for the next element or number


# Q72. What is the use of break statement?
# ANS:
# Break Statement is a loop control statement that is used to terminate the loop.


# Q73. What is the use of pass statement?
# ANS:
# The pass statement is used as a placeholder for future code. When the pass statement is executed, 
# nothing happens, but you avoid getting an error when empty code is not allowed


# Q74. What is the use of range() function?
# ANS:
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number.

# Q75. How can you loop over a dictionary?
# ANS:
# You can loop through a dictionary by using a for loop. When looping through a dictionary, 
# the return value are the keys of the dictionary, but there are methods to return the values as well.



# Q76. Write a Python program to find the factorial of a given number.
# CODE:
fact=1
num=5
for i in range(1,num + 1):
    fact = fact*i
print("The factorial of",num,"is",fact)



# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
# CODE:
p,r,n=100,4,6
si=(p*r*n)/100
print("The simple intrest is : ",si)


# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
# CODE:

def compound_interest(principal, rate, time):

	# Calculates compound interest
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("Compound interest is", CI)

compound_interest(10000, 10.25, 5) #Calling the function



# Q79. Write a Python program to check if a number is prime or not.
# CODE:

num=44
count=0
for i in range(2,num//2):
    if num%i==0:
        print("Number is not prime by it is divisible of ",i)
        count=1
        break
if count==0:
    print("Number is prime")


# Q80. Write a Python program to check Armstrong Number.
# CODE:
sum=0
num =153
temp = num
while temp>0:
    digit= temp%10
    sum=digit**3 + sum
    temp=temp//10

if sum == num:
    print("No is Armstrong")
else:
    print("No is not Armstrong")



# Q81. Write a Python program to find the n-th Fibonacci Number.
# CODE:
n=int(input("Enter the number"))
a,b=1,1
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
print(c)




# Q82. Write a Python program to interchange the first and last element in a list.
# CODE:
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))



# Q83. Write a Python program to swap two elements in a list.
# CODE:
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))



# Q84. Write a Python program to find N largest element from a list.
# CODE:
def Nmaxelements(list1, N):
	final_list = []

	for i in range(0, N):
		max1 = 0
		
		for j in range(len(list1)):	
			if list1[j] > max1:
				max1 = list1[j];
				
		list1.remove(max1);
		final_list.append(max1)
		
	print(final_list)

# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(list1, N)


        

# Q85. Write a Python program to find cumulative sum of a list.
# CODE:
def Cumulative(lists):
	cu_list = []
	length = len(lists)
	cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
	return cu_list[1:]

lists = [10, 20, 30, 40, 50]
print (Cumulative(lists))


# Q86. Write a Python program to check if a string is palindrome or not.
# CODE:
n=1221
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")



# Q87. Write a Python program to remove i'th element from a string.
# CODE:
i=5
str1='BigDataBootCAmp'
a=str1[:i]
b=str1[i+1:]
print(a+b)



# Q88. Write a Python program to check if a substring is present in a given string.
# CODE:
a= 'BigDataBootcamp2.0'
b='Data'
print(b in a)


# Q89. Write a Python program to find words which are greater than given length k.
# CODE:
length=5
lst1=['Furquan','go','above','null','below','iNeuron','come']
lst2=[]
for i in lst1:
    if len(i)>length:
        lst2.append(i)
print(lst2)


# Q90. Write a Python program to extract unquire dictionary values.
# CODE:
my_dict = {"apple": 5, "banana": 2, "orange": 5, "kiwi": 1, "pear": 3}

unique_values = list(set(my_dict.values()))

print("Unique dictionary values:")
for value in unique_values:
    print(value)


# Q91. Write a Python program to merge two dictionary.
# CODE:
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)
print(dict_3)


# Q92. Write a Python program to convert a list of tuples into dictionary.
# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# CODE:
def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di
	
# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
	("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))



# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]
# CODE:

# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple
list1 = [1, 2, 5, 6]
# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]
print(res)




# Q94. Write a Python program to get all combinations of 2 tuples.
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# CODE:
# Python3 code to demonstrate working of
# All pair combinations of 2 tuples
# Using list comprehension
# initializing tuples
test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

# printing original tuples
print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

# All pair combinations of 2 tuples
# Using list comprehension
res = [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a, b) for a in test_tuple2 for b in test_tuple1]

# printing result
print("The filtered tuple : " + str(res))



# Q95. Write a Python program to sort a list of tuples by second item.
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# CODE:
def Sort_Tuple(tup):

    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

# Driver Code
tup = [('for', 24), ('is', 10), ('Geeks', 28),('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
print(Sort_Tuple(tup))



# Q96. Write a python program to print below pattern.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# CODE:
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=" ")
    print()


# Q97. Write a python program to print below pattern.
#     *
#    **
#   ***
#  ****
# *****
# CODE:
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print('*',end=" ")
    print()




# Q98. Write a python program to print below pattern.

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# CODE:
def triangle(n):
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)




# Q99. Write a python program to print below pattern.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# CODE:
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")

    print()

# Q100. Write a python program to print below pattern.
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# CODE:
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")

    print()





