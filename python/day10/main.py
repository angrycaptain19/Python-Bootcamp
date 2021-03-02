# #function with outputs

# def format_name(f_name,l_name):
#    print( f_name.title())
#    print(l_name.title())
    
# format_name("rishav","ayushi")

# def format_name(f_name,l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} and {formated_l_name}"

# print(format_name("rishav","ayushi"))


# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "Invalid Data."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f" Result {formated_f_name} and {formated_l_name}"

# print(format_name(input("Enter Your First Name: "),input("Enter Your Partner Name: ")))


#Problem
#Sol

def is_leap(year):
    """
    Check Leap Year
    """
    if year % 4 == 0:
        return year % 400 == 0 or year % 100 != 0
    else:
        return False
  
def days_in_month(year,month):
    
  
   
  if month > 12 or month <1:
      return "Invalid Data"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
      return 29
  return month_days[month-1]
    
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


is_leap()

   


