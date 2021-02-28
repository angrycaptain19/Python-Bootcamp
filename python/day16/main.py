from turtle import Turtle, Screen
from prettytable import PrettyTable

# turtle Module
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.right(270)
timmy.forward(100)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


# preetytable package

# table = PrettyTable()
#
# table.add_column("Pokemon Name",
#                  [
#                      "Pikachu",
#                      "Squirtle",
#                      "Charmander"
#                   ])
#
# table.add_column("Type",
#                  [
#                      "Electric",
#                      "Water",
#                      "Fire"
#                   ])
#
# table.align = "l"
# print(table)
