# import random

# # # Problem-1

# # # You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".


# # # num = random.randint(0,1)
# # # if num == 1:
# # #     print("Heads")
# # # else:
# # #     print("Tails")


# # #Lists in Python

# # # Lists


# # states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
# #                      "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# # # Problem-2
# # # You are going to write a program which will select a random name from a list of names.
# # # The person selected will have to pay for everybody's food bill.

# # Solution

# # names_string = input("Give Me Everybody's Name, Seperated By a comma. ")
# # names = names_string.split()  # split() function is use to make a lits.


# # # num_person = len(names) # lem() find the length of items in list.
# # # random_number = random.randint(0, num_person-1) # random.randiant(0,num_person-1) :- 0 is starting and num_person-1 is -1 from last value.

# # # random_names = names[random_number] #names[random number]
# # # print(random_names) #output:- everytime chnage. Anish sometimes Rishav , etc.


# # # we can also write this code using choice() function.
# # # solution

# # # choice() direct choose the random value from lists.
# # random_names = random.choice(names)
# # print(random_names)


# # Problem-3
# # You are going to write a program which will mark a spot with an X.

# # In the starting code, you will find a variable called map.

# # This map contains a nested list.
# # When map is printed this is what the nested list looks like:

# #['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# # In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# # ['⬜️', '⬜️', '⬜️']
# # ['⬜️', '⬜️', '⬜️']
# # ['⬜️', '⬜️', '⬜️']

# # Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

# # Solution

# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Enter the Position: ")

# horizontal = int(position[0])
# vertical = int(position[1])

# change_v = map[vertical-1]
# change_v[horizontal-1] = "*"

# print(f"{row1}\n{row2}\n{row3}")
