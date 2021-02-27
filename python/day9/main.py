# # # # # Python Dictionary


# # # # {key:value}
# # # # programming_dictionary = {
# # # #     "Bug":"A error in a program that process the program from running as expected.",
# # # #     "Function": "A piece of code that you can easily call over and over again.",
# # # # }

# # # # #Retrieving items from dictionary.
# # # # print(programming_dictionary["Function"])



# # # #Problme-1
# # # You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# # # Write a program that converts their scores to grades. By the end of your program, you should have 
# # # a new dictionary called student_grades that should contain 
# # # student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.


# # #Solution


# # # student_scores ={
# # #     "Harry":81,
# # #     "Ron": 78,
# # #     "Hermione": 99,
# # #     "Draco": 74,
# # #     "Naville": 62,
# # # }

# # # student_grades = {}
# # # for student in student_scores:
# # #     score = student_scores[student]
# # #     if score > 90:
# # #         student_grades[student] = "Outstanding"
# # #     elif score > 80:
# # #         student_grades[student] = "Excellent"
# # #     elif score > 70:
# # #         student_grades[student] = "Acceptable"
# # #     else:
# # #         student_grades[student] = "Fail"
# # # print(student_grades)



# # #Nested Dictionary

# # # travel_log = {
# # #     "Sikkim": {"place_visited": ["silliguri","gangtok"], "total_visit":2},
# # #     "north_sikkim": ["Lanchong", "Yumthang"]
# # # }
# # # print(travel_log)


# # #Nested Dictionary in a list


# # travel_log = [
# #     {
# #         "state": "sikkim",
# #         "cities_visted": ["Gangtok","yumthang","lachong"],
# #         "total_visits": 3
# #     },
# #     {
# #         "state": "bihar",
# #         "cities_visted": ["patna","gaya","bihar_sharif"],
# #         "total_visits":3

# #     }
# # ]


# # print(travel_log)



# #problem


# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country,visits,cities):
#     # travel_log.append(
#     #     {
            
#     #      "country": country,
#     #      "visits": visits,
#     #      "cities": cities
#     #     }
#     # )
#     new_country ={}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)



