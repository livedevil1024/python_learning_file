# Coffee Machine Menu with Ingredients

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,          # ml
            "milk": 0,
            "coffee": 12,         # grams
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 50,          # ml
            "coffee": 18,         # grams
            "milk": 150,          # ml
        },
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,          # ml
            "coffee": 18,         # grams
            "milk": 100,          # ml
        },
        "cost": 3.00
    }
}

resources = {
    "water": 300,
    "milk" :200,
    "coffee":100
}
Money = 0

def report():
    print("Water remaining in the Machine is :",{ resources["water"] })
    print("Milk remaining in the Machine is :",{ resources["milk"] })
    print("Coffee remaining in the Machine is :",{ resources["coffee"] })
    print("The profit has been made is:", Money)

def check_resource(coffee_1):
    if (resources["water"]- MENU[coffee_1]["ingredients"]["water"]) < 0:
        print("resources is insufficient, sorry there is not enough water")
        reorder = input("Would you like to have something else? Y/N").lower()
        if reorder == 'n':
            print("Have a good day")
            quit()
        return False
    elif(resources["coffee"]- MENU[coffee_1]["ingredients"]["coffee"])<0:
        print("resources is insufficient, sorry there is not enough coffe")
        reorder = input("Would you like to have something else? Y/N : ").lower()
        if reorder == 'n':
            print("Have a good day")
            quit()
        return False
    elif(resources["milk"]- MENU[coffee_1]["ingredients"]["milk"]) < 0:
        print("resources is insufficient, sorry there is not enough milk")
        reorder = input("Would you like to have something else? Y/N").lower()
        if reorder == 'N':
            print("Have a good day")
            quit()
        return False
    else:
        return True
    
def coffe_formation(coffee_2):
    resources["water"] -= MENU[coffee_2]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_2]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee_2]["ingredients"]["milk"]

def Ask_money(coffee_3):
    quater = int(input("Enter the number of quaters: "))
    dime = int(input("Enter the number of dime: "))
    nickel = int(input("Enter the number of nickles: "))
    pennies = int(input("Enter the number of pennies: "))
    
    total_customer_money = (0.25 * quater) + (0.1 * dime) + (0.05 * nickel) + (0.01 * pennies)
    if total_customer_money < int(MENU[coffee_3]["cost"]):
        print(f"your {total_customer_money} is insufficeient for th ordered coffee ")
        return False
    else :
        remaning_amount = round(total_customer_money - MENU[coffee_3]["cost"],2)
        print(f"here is your change {remaning_amount}")
        global Money 
        Money += MENU[coffee_3]["cost"]
        return True

def order(coffee_0):

    if coffee_0 == "off":
        quit()
    elif coffee_0 == "report":
        report()
        Menu()
    elif not check_resource(coffee_0):
        Menu()
    elif not Ask_money(coffee_0):
        Menu()
    else :
        coffe_formation(coffee_0)
        print(f"your {coffee_0} is been made")
        Menu()  



def Menu():
    customer_request =str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    order(customer_request)
 
Menu()