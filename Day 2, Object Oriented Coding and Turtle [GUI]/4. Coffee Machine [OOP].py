from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
print(menu.get_items())
print(menu.find_drink("latte").ingredients["water"])
