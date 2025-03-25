from data import MENU,resources,coins,logo_distributeur,emoji_cafe

def report(stock):
    for resource,quantite in stock.items():
        if resource=="money":
            print(f"{resource}: ${quantite}")
        elif resource=='coffee':
            print(f"{resource}: {quantite}g")
        else:
            print(f"{resource}: {quantite}ml")


def stock_is_empty (stock):
    co=0
    for resource,qte in stock.items():
        if resource!="money" and qte==0:
            co+=1
    if co==0:
        return False
    else:
        return True



print("Welcome tou our new coffe machine ")

while True:
    if stock_is_empty(resources):
        print("the machine of coffe is out of stock ")
        break
    repoonse=input("what would you like ?(cappuccino/espresso/latte):")
    
    if repoonse=="report":
        report(resources)
    else:
        print("please insert coins ")
        coffee_name=repoonse
        coffe_price=MENU[coffee_name]["cost"]
        print(coffe_price)

        quarters=int(input("enter the number of quarters: "))
        dimes=int(input("enter the number of dimes: "))
        nickles=int(input("enter the number of nickles: "))
        pennies=int(input("enter the number of pennies: "))

        somme=quarters*coins["quarter"]["value"]+dimes*coins["dime"]["value"]+nickles*coins["nickle"]["value"]+pennies*coins["penny"]["value"]
        money_in_change=somme-coffe_price

        if money_in_change<0:
            print("you didnt insert enough money")
        else:
            print(f"your {coffee_name} is ready ")
            print(f"money in change ${money_in_change:02f}")
            print(emoji_cafe)
            


            if coffee_name!="esspreso":
                resources["milk"]-=MENU[coffee_name]["ingredients"]["milk"]
                resources["coffee"]-=MENU[coffee_name]["ingredients"]["coffee"]
                resources["water"]-=MENU[coffee_name]["ingredients"]["water"]
                resources["money"]+=MENU[coffee_name]["cost"]
            elif coffee_name=="esspresso":
                resources["coffee"]-=MENU[coffee_name]["ingredients"]["coffee"]
                resources["water"]-=MENU[coffee_name]["ingredients"]["water"]
                resources["money"]+=MENU[coffee_name]["cost"]
        quitter=input("press (Q) if you dont want to purhcase coffee again").lower()
        if quitter=="q":
             break

    

    
    

    




    
    




