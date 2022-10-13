def coffeeSelect():
    print(""">>>What would you like?
          \n\tMenu:
          \n\t\tEspresso
          \n\t\tLatte
          \n\t\tCappuccino\n<<<""", end = "")
    coffee = input()
    return coffee

def coinInput():
    print(""">>>Enter coin""")
    print("\tEnter cents")

resources = {"water": 300, "coffee" : 300, "milk": 240, "money": 0} #Inital condition

recipe = {
"espresso": {"water": 50, "coffee": 18, "milk": 0, "money": 2},
"latte": {"water": 200, "coffee": 24, "milk": 150, "money": 1},
"cappuccino": {"water": 250, "coffee": 24, "milk": 100, "money": 10}
}

def report():
    print("xxxxxxxxxxxxxxxx")
    print(f"""Report\n
          Water left: {resources["water"]}\n
          Milk left: {resources["milk"]}\n
          Coffee left: {resources["coffee"]}\n
          Money made: ${resources["money"]}""")
    print("") 
    print("xxxxxxxxxxxxxxxx")
    
coffeeSel = coffeeSelect()

def resourcesLeft(coffeeSel):
    water = resources["water"] - recipe[coffeeSel]["water"]
    coffee = resources["coffee"] - recipe[coffeeSel]["coffee"]
    milk = resources["milk"] - recipe[coffeeSel]["milk"]
    
    
    if(water >= 0 and coffee >= 0 and milk >= 0):
        money = resources ["money"] + recipe[coffeeSel]["money"]

        resources["money"] = money
        resources["water"] = water
        resources["milk"] = milk
        resources["coffee"] = coffee
        
        return True
    
    else:
        return False

report
if(resourcesLeft("latte")):
    report()
else:
    print("insufficient resources")
