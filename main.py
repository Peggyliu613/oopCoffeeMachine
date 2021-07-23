from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

peggyMenu = Menu()
peggyCoffeeMaker = CoffeeMaker()
peggyMoneyMachine = MoneyMachine()

while True:
    print("What would you like?")
    action = input()

    if action == "off":
        print("turning off the machine")
        break
    elif action == "report":
        peggyCoffeeMaker.report()
        peggyMoneyMachine.report()
    else:
        if peggyCoffeeMaker.is_resource_sufficient(peggyMenu.find_drink(action)):
            if peggyMoneyMachine.make_payment(peggyMenu.find_drink(action).cost):
                peggyCoffeeMaker.make_coffee(peggyMenu.find_drink(action))