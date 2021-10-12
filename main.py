from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
kahvi = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like?: ")
    if choice == 'off':
        is_on = False
    if choice == 'report':
        kahvi.report()
        money.report()
    if choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
        drink = menu.find_drink(choice)
        drink_ingredients = drink.ingredients
        drink_cost = drink.cost
        print(drink, drink_cost, drink_ingredients)
        if kahvi.is_resource_sufficient(drink):
            if money.make_payment(drink_cost):
                kahvi.make_coffee(drink)
