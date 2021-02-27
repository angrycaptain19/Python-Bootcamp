# #Function with User Inputs.

# def user_name(name):
#     print(f"Hello {name}")

# user_name("Rishav Raj")


#Problem-1
#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
#Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 ✖️ 4) ÷ 5

#Solution

# def paint_house(height,width,coverage):
#     number_of_cans = round((height*width)/coverage)
#     print(f"The Number of Cans is: {number_of_cans}")


# test_h = int(input("Enter Your height: "))
# test_w = int(input("Enter Your Width: "))
# test_c = int(input('Enter Your Coverage: '))
# paint_house(height=test_h,width=test_w,coverage=test_c)




#Problem-2 Prime numbers are numbers that can only be cleanly divided by itself and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.


def prime_number(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime Number.")
    else:
        print("It is not a prime Number.")
    
n = int(input("Enter a Number: "))
prime_number(number=n)