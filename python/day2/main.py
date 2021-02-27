# Day-2 Data Type

# String
print("Hello"[4])
# output = o
print("111" + "111")
# output = 111111

# Integers
print(111 + 111)
# output = 222
# Larger Integers is shown by 123_456_789


# Float
3.14159

# Boolean
True
False


# Type() function is use to check which data type is this.

num_char = len(input("What is Your Name? "))
# print("Your Name has " + num_char + "char")
# output = TypeError: can only concatenate str (not "int") to str.

# for solve above error, we convert the int data type to string data type.
new_num_char = str(num_char)
print("Your Name has " + new_num_char + " char")
# output = Your Name has 6 char

print(type(num_char))
# output = <class 'int'>


# Problem-1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8.

# Solution-1

numb = input("Enter The Number: ")

num1 = int(numb[0])
num2 = int(numb[1])
add_num = (num1 + num2)

print(add_num)


# Mathematical Operation in Python

# 3 + 2
# 3 - 2
# 3 * 2
# 6 / 3
# 2 ** 3

# PEMDAS
#P=parantheses ()
# E=exponents **
# M=multiplication *
# D=division /
# A=additions +
# S=subtractions -


# Problem-2
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# Solution-2

weight = int(input("Enter Your Weight in kg: "))
height = float(input("Enter Your Height in m: "))

bmi = round(weight/height**2)

print(bmi)


# Round() function is used to round the number

print(round(8/3))
#output = 3
print(round(8/3, 2))
#output = 2.67


result = 4/2
print(result)
output = 2.0

result = 4//2
print(result)
output = 2
# (// ) is used for round the number. convert float to int data type.

result = 4/2
result /= 2
# result/=2 === result = result / 2
print(result)

score = 0
# score = score + 1
# print(score)
#output = 1

score += 1
print(score)
#output = 1


# f-string is help us to not convert everytime to same data type to print.

score = 1
height = 1.0
isSwimming = True

print(
    f"Your Score is {score}, Your Height is {height}, Your Swimming is {isSwimming}.")

# output = Your Score is 1, Your Height is 1.0, Your Swimming is True.


# # Problem-3
# # Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# # Solution-3

age = int(input("Enter Your Age: "))

days = (90-age)*365
weeks = (90-age)*52
months = (90-age)*12

print(f"You have {days} Days, {weeks} Weeks, {months} Months Left.")
