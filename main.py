from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_dict = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def report():
    for resource, value in resources.items():
        print(f"{resource.title()} : {value}")


def halt_machine():
    print("Machine halted.")
    return exit(0)


def is_resource_sufficient(coffee_ingredients, resource):
    for ingredient, value in resource.items():
        if coffee_ingredients[ingredient] > value:
            return False
    return True


def process_coffee(coffee_ingredients, resource):
    for ingredient, value in resource.items():
        resource[ingredient] = value - coffee_ingredients[ingredient]
    return resource


def process_coins(coffee_cost):
    print("Insert your coins.")
    # monetary = 0
    quarters = int(input("How many quarters? $"))
    dimes = int(input("How many dimes? $"))
    nickles = int(input("How many nickles? $"))
    pennies = int(input("How many pennies? $"))
    monetary = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(monetary, coffee_cost)
    if coffee_cost > monetary:
        print("Sorry, not enough money.")
        return str
    # elif coffee_cost <= money_insert:
    #     return f"Sorry,"
    return monetary - coffee_cost


def is_coins_sufficient(coffee_cost, money_payment):
    if type(coffee_cost) == str:
        return
    if coffee_cost <= money_payment:
        return True


def make_coffee():
    global resources
    coffee_types = ""
    for type_coffee in MENU:
        coffee_types += type_coffee + "/"
    coffee_choice = "latte"  # input(f"What would you like? {coffee_types}")
    ingredients = MENU[coffee_choice]['ingredients']
    price_coffee = MENU[coffee_choice]["cost"]
    if coffee_choice == "off":
        halt_machine()
    elif coffee_choice == "report":
        report()
    elif is_resource_sufficient(ingredients, resources):
        process_coffee(ingredients, resources)
        payment = process_coins(price_coffee)
        print(payment)
        if is_coins_sufficient(price_coffee, payment):
            print("Enjoy your coffee!)")
            print(resources)
        else:
            print("Not works")

    # return coffee_choice


make_coffee()
