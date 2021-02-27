# # Day-3
# # Conditional Statement.


# # Problem-1
# # Write a program that works out whether if a given number is an odd or even number.

# num = int(input("Enter The Number: "))

# if num % 2 == 0:
#     print(f"The {num} is Even Number.")
# else:
#     print(f"The {num} is Odd Number.")


# # Problem-2
# # Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# # It should tell them the interpretation of their BMI based on the BMI value.

# # Under 18.5 they are underweight
# # Over 18.5 but below 25 they have a normal weight
# # Over 25 but below 30 they are slightly overweight
# # Over 30 but below 35 they are obese
# # Above 35 they are clinically obese.


# weight = int(input("Enter Your Weight: "))
# height = float(input("Enter Your Height: "))


# bmi_weight = weight/height**2

# if bmi_weight < 18.5:
#     print("You Are underweight")
# elif bmi_weight < 25:
#     print("You Are normal weight ")
# elif bmi_weight < 30:
#     print("You Are slightly overweight")
# elif bmi_weight < 35:
#     print("You Are obese ")
# else:
#     print("You are  clinically obese. ")


# Problem-3
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:


# year = int(input("Enter The Year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a Leap Year")
#         else:
#             print(f"{year} is Not a Leap Year")
#     else:
#         print(f"{year} is a Leap year")
# else:
#     print(f"{year} is Not a Leap Year")


# Promblem-4
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1


# print("Welcome to Dhooni Pizza Shop")

# pizza_size = input("What Pizza Size You Want 'S','M', and 'L'?  ")
# add_pepperoni = input("Do You Want pepperoni 'Y' or 'N' ? ")
# extra_cheese = input("Do You Want Extra Cheese 'Y' or 'N' ? ")

# bill = 0

# if pizza_size == "S":
#     bill += 15
# elif pizza_size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if pizza_size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1
# print(f"Your Bill is {bill}")


# Problem-5

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
