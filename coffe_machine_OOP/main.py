from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

notre_menu=Menu()
machine_a_cafer=CoffeeMaker()
machine_a_sous=MoneyMachine()

while True:
    reponse=input(f"what would you like ? {notre_menu.get_items()}: ")
    if reponse=="report":
        machine_a_cafer.report()
        machine_a_sous.report()
    drink=notre_menu.find_drink(reponse)
    mon_argent=machine_a_sous.process_coins()
    drink_price=drink.cost
    if machine_a_cafer.is_resource_sufficient(drink):
        if machine_a_sous.make_payment(drink_price):
            machine_a_cafer.make_coffee(drink)