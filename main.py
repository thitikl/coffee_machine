from data import MENU, resources

def report():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${money}")

def check_resource(input):
  order_water = MENU[input]["ingredients"]["water"]
  order_coffee = MENU[input]["ingredients"]["coffee"]
  if input == "espresso":
    order_milk = 0
  else:
    order_milk = MENU[input]["ingredients"]["milk"]
  
  if resources["water"] > order_water:
    if resources["milk"] > order_milk:
      if resources["coffee"] > order_coffee:
        return True
      else:
        print("Sorry. Not enough coffee")
        return False
    else:
      print("Sorry. Not enough milk")
      return False
  else:
    print("Sorry. Not enough water")
    return False

    
 
def check_money(drink):
  print("please insert coins.")
  quaters = int(input("How many quaters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickels?: "))
  pennies = int(input("How many pennies?: "))
  total_insert_coin = (quaters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)

  drink_cost = MENU[drink]["cost"]

  if total_insert_coin < drink_cost:
    print("Not enough money. Money refunded")
    return False
  else:
    change = round(total_insert_coin - drink_cost,2)
    print(f"Here is your change ${change}")
    print(f"Here is your {drink}. Enjoy!")
    return True

def remain_resource(coffee):
  water_using = MENU[coffee]["ingredients"]["water"]
  coffee_using = MENU[coffee]["ingredients"]["coffee"]
  if coffee != "espresso":
    milk_using = MENU[coffee]["ingredients"]["milk"]
  else:
    milk_using = 0
  resources["water"] -= water_using
  resources["coffee"] -= coffee_using
  resources["milk"] -= milk_using

  return resources


money = 0.0
end_process = False

while not end_process:
  user_command = input("What would you like? (espresso/latte/cappuccino): \n").lower()

  if user_command == "report":
    report()
  elif user_command == "espresso" or user_command == "latte" or user_command == "cappuccino":
    if check_resource(user_command):
      if check_money(user_command):
        money += MENU[user_command]["cost"]
        remain_resource(user_command)
  elif user_command == "off":
    end_process = True
  else:
    print("Please select valid drink you'd like.")


  
