# Question No :: 01
# • Declare and initialize two variables, num1 and num2, with integer values. Calculate and print 
# their sum

x = int(input("Enter the First Value: ", ))
y = int(input("Enter the Second Value: ", ))
addition = x + y
print(f"The sum of two numbers is: ", addition)

# Q2)Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message. Explore basic string operations in Python.

a = "My "
a += "World!"
print(a)

# Q3)Declare a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. Learn to use boolean variables for decision-making in Python

is_python_a_language = True
if is_python_a_language:
    print("Python is intresting.")
else:
    print("Python is Boaring Language.")

# Q4) Create a list called fruits with at least three different fruit names. Print the list, add a new fruit, and then print the updated list. Understand the basics of working with lists in Python

fruits = ["cherry","apple","kiwi"]
print("List of Fruits: ", fruits)
fruits.append("mango")
print("List of Updated Fruits: ", fruits)

#Q5)Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values. Explore how to convert between different data types in Python

#Current Value
price = float(input("Enter a decimal number: "))
print("Current Value is:", price)

# # Converting DEC into INT:
integer_price = int(price)
print("The converted price is: ", integer_price)

#Q6)Create a dictionary named student_info with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary. Learn how to work with dictionaries, a versatile data structure in Python
std = {'Qasim' : 23: C, 'Ali' : 25: B+,}
print("The dictionary of students:", std)

# # Question No :: 07
# Write a program that takes user input for their age and prints a message addressing their age 
# group (e.g., "Teenager," "Adult").

# create user input for thier age
user = int(input("Enter you age : "))
# # check if user age is teenager or adult
if user < 13:
    print("You are Kid")
elif user < 20:
    print("You are Teenager")
else:
    print("You are Adult")


# Question No :: 08
# • Define a complex number variable, comp_num, with a real and imaginary part. Print both parts 
# separately

# create a complex number variable
comp_num = 6+5j
# print both parts separately real and imaginary .
print("Real part of complex number :",comp_num.real)
print("Imaginary part of complex number :",comp_num.imag)


# Question No :: 09
# Combine two strings using string concatenation, and then use string interpolation to include the 
# length of the resulting string in a print statement.

# # create a two variable and assing two string values.
str1 = "Abdul Aziz"
str2 = " Nagarseth"
# # concatenation two string and there length is 
combine = str1 + str2
print(f"Combine string is that : \"{combine}\".Its lenght : {len(combine)}")

# Question No :: 10
# Create a tuple, days_of_week, with the names of the days. Access and print the third day of the 
# week.

# # Create a tuple
days_of_week = ("Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

# # if you access and print the forth day of the week.
forth_day = days_of_week[3]
# print third day
print("Third day of the week is that ::",forth_day)
