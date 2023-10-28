MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}
    """)


def check_resources(coffee):
    if int(MENU[coffee]["ingredients"]["water"]) > int(resources["water"]):
        return "Sorry, there is not enough water."
    elif coffee != "espresso" and int(MENU[coffee]["ingredients"]["milk"]) > int(resources["milk"]):
        return "Sorry, there is not enough milk."
    elif int(MENU[coffee]["ingredients"]["coffee"]) > int(resources["coffee"]):
        return "Sorry, there is not enough coffee."
    else:
        return True


def subtract_resources(coffee):
    if coffee != 'espresso':
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]

    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def process_money(quarters, dimes, nickles, pennies):
    total_value = 0
    total_value += int(quarters) * 0.25
    total_value += int(dimes) * 0.10
    total_value += int(nickles) * 0.05
    total_value += int(pennies) * 0.01

    return total_value


machine_state = "on"
money = 0

while machine_state == "on":
    response = input("What would you like? (espresso/latte/cappuccino): ")

    if response == "espresso":
        if check_resources("espresso"):
            print("Please, insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))

            user_money = process_money(quarters, dimes, nickles, pennies)

            if user_money >= MENU["espresso"]["cost"]:
                money += float(MENU["espresso"]["cost"])
                if user_money - MENU["espresso"]["cost"] > 0:
                    change = user_money - MENU["espresso"]["cost"]
                    print(f"Here is ${round(change, 2)} dollars in change.")
                subtract_resources("espresso")
                print("Here is your espresso. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(check_resources("espresso"))

    elif response == "latte":
        if check_resources("latte"):
            if check_resources("latte"):
                print("Please, insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))

                user_money = process_money(quarters, dimes, nickles, pennies)

                if user_money >= MENU["latte"]["cost"]:
                    money += float(MENU["latte"]["cost"])
                    if user_money - MENU["latte"]["cost"] > 0:
                        change = user_money - MENU["latte"]["cost"]
                        print(f"Here is ${round(change, 2)} dollars in change.")
                    subtract_resources("latte")
                    print("Here is your latte. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print(check_resources("latte"))

    elif response == "cappuccino":
        if check_resources("cappuccino"):
            if check_resources("cappuccino"):
                print("Please, insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))

                user_money = process_money(quarters, dimes, nickles, pennies)

                if user_money >= MENU["cappuccino"]["cost"]:
                    money += float(MENU["cappuccino"]["cost"])
                    if user_money - MENU["cappuccino"]["cost"] > 0:
                        change = user_money - MENU["cappuccino"]["cost"]
                        print(f"Here is ${round(change, 2)} dollars in change.")
                    subtract_resources("cappuccino")
                    print("Here is your cappuccino. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print(check_resources("cappuccino"))

    elif response == "report":
        print(report())

    elif response == "off":
        print("Turning down machine...")
        machine_state = "off"