machineStatus = True

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
          Water left: {resources["water"]}ml\n
          Milk left: {resources["milk"]}ml\n
          Coffee left: {resources["coffee"]}mg\n
          Money made: ${resources["money"]}""")
    print("") 
    print("xxxxxxxxxxxxxxxx")
    

def resourcesLeft(coffeeSel):

    if(coffeeSel == "report"):
        report()
    
    elif(coffeeSel in recipe.keys()):

        moneyEntered = moneyManager()
        
        if(recipe[coffeeSel]["money"] <= moneyEntered):
            
            water = resources["water"] - recipe[coffeeSel]["water"]
            coffee = resources["coffee"] - recipe[coffeeSel]["coffee"]
            milk = resources["milk"] - recipe[coffeeSel]["milk"]
            
            depletedResource = []
            resourcesValues = [water, coffee, milk]
            resourcesName = ["water", "coffee", "milk"]
            
            for i in range(3):
                if(resourcesValues[i] <= 0):
                    depletedResource.append(resourcesName[i])
                    
            if(water >= 0 and coffee >= 0 and milk >= 0):
                money = resources ["money"] + recipe[coffeeSel]["money"]
                moneyOut = moneyEntered - recipe[coffeeSel]["money"]
                print(f"Here is change: ${moneyOut}")
                resources["money"] = money
                resources["water"] = water
                resources["milk"] = milk
                resources["coffee"] = coffee
                
                return True
            
            else:
                print("Sorry there is not enough:")
                
                for i in depletedResource:
                    print(f"\t{i}")
                    
        else:
            print(f"Not enough money entered, Here is your refund: {moneyEntered}")
    
    else:
        print("Cannot process the input provided!\nPlease try again...")

def moneyManager():
    print(">>>Please enter coins\n>>>Enter Pennies\n\t<<<", end = "")
    pennies = int(input())
    print(">>>Enter Nickels\n\t<<<", end = "")
    nickels = int(input())
    print(">>>Enter Dimes\n\t<<<", end = "")
    dimes = int(input())
    print(">>>Enter Quarters\n\t<<<", end = "")
    quarters = int(input())
    
    return(pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25)
    
    
    
    

def coffeeOrder():
    
    while(machineStatus):
        coffeeSel = coffeeSelect()
        coffeeSel = coffeeSel.lower()
        
        if(coffeeSel == "off"):
            print("Machine turning off...")
            break
        
        else:
            
            resourcesLeft(coffeeSel)
    
        


#TODO: add Quarters, Dimes, Nickles, Pennies - Done
#TODO: Add off
#TODO: Add report as coffee select option - Done
#TODO: Fix Initial Resources, Recipe, and, Money Earned.
#Quarter: 0.25, Dimes: 0.1, Nickel: 0.05, Penny: 0.01

coffeeOrder()