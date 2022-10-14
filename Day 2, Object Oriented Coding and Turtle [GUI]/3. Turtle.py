from prettytable import PrettyTable


from turtle import Turtle, Screen


arry = Turtle()

print(arry)

myScreen = Screen()

print(myScreen.canvheight)
print(myScreen.canvwidth)

arry.shape("turtle")
arry.color("blue2")
arry.forward(100)
arry.left(90)
arry.forward(100)
arry.goto(0, 100)
arry.goto(0, 0)
arry.goto(100, 100)



myScreen.exitonclick()



table = PrettyTable()
table.align = "r"
table.title = "Deutsche übersicht"
table.add_column("Gender", ["Masc", "Femm", "Neut"])
table.add_column("Das", ["Der", "Die", "Das"])
table.add_column("Es", ["Er", "Sie", "Es"])
table.add_column("Ein", ["Ein", "Eine", "Ein"])

print(table)