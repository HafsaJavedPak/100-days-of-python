
# define resources
resources = {
    "water" : {
        "unit" : "ml",
        "amount" : 300
    },
    "milk" : {
        "unit" : "ml" ,
        "amount" : 200
    },
    "coffee" : {
        "unit" : "g",
        "amount" : 100
    }
}



# dictionary to store the recipe
coffees = {
    "espresso": {
        "price" : {
            "unit" : "usd",
            "amount" : 1.50
        },
        "water": {
            "unit": "ml",
            "amount": 15
        },
        "coffee": {
            "unit": "g",
            "amount": 18
        }
    },
    "latte": {
        "price" : {
            "unit" : "usd",
            "amount" : 2.50
        },
        "water": {
            "unit": "ml",
            "amount": 200
        },
        "coffee": {
            "unit": "g",
            "amount": 24
        },
        "milk": {
            "unit": "ml",
            "amount": 150
        }
    },
    "cappuccino": {
        "price" : {
            "unit" : "usd",
            "amount" : 3.00
        },
        "water": {
            "unit": "ml",
            "amount": 250
        },
        "coffee": {
            "unit": "g",
            "amount": 24
        },
        "milk": {
            "unit": "ml",
            "amount": 100
        }
    }
}




# print report function
def report () :
    for item, details in resources.items() :
        print(f"\t{item.title()} : {details['amount']} {details['unit']}")



# validates if coffe can be made
def validate_coffee(coffee_name: str) -> bool:
    try:
        
        coffee_components = coffees[coffee_name]
        
        for ingredient, details in coffee_components.items():
            if ingredient == "price":
                continue
            if details["amount"] <= resources[ingredient]["amount"]:
                continue
            else:
                return False
        return True
    except KeyboardInterrupt:
        print("This coffee is not available.")
        return False
    
# validate_coffee("latte")


def validate_money(amount : int, coffee:str) -> False:
    if amount > coffees[coffee]["price"]["amount"]:
        print(f"Refunding ${amount - coffees[coffee]["price"]["amount"]}.")
        return True
    elif amount == coffees[coffee]["price"]["amount"]:
        return True
    else : 
        print(f"Insufficient payment. ${amount} refunded.")
        return False



# ask for coins and drink
def ask_order(coffee) -> {bool, str or None}:
    if validate_coffee(coffee_name=coffee):
        print("Enter payment please.")
        penny = float(input("\tPenny : "))/100
        dime = float(input("\tDime : "))/100
        nickel = float(input("\tNickel : "))/100
        quarter = float(input("\tQuarter : "))/100
        money = penny + dime + nickel + quarter
        if validate_money(amount=money,coffee=coffee):
            print("Making Coffee.....")
            return (True, coffee)
        else:
            return (False, None)
    else :
        return (False, None)

    


# if transaction successful, then make coffee
def make_coffee(coffee_name) -> None:
    temp_coffee = coffees[coffee_name].copy()
    temp_coffee.pop("price",None)
    # for item, details in temp_coffee.items() :
        # resources[item]["amount"] -= details['amount']
    
    print("Here is your latte ☕. Enjoy!")

make_coffee("latte")


import sys
if __name__ == "__main__":
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        
        if choice == "report":
            report()
        elif choice == "off":
            print("Turning coffee machine OFF.")
            sys.exit(0)
        elif choice in ["espress","latte","cappuccino"]:           
            print("hi") 
            can_make_coffee, coffee_name1 = ask_order(choice)
            if can_make_coffee == True:
                make_coffee(coffee_name=coffee_name1)
        else:
            print("Invalid option selected. Please try again.")





