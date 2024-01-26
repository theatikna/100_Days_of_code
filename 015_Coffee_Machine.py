class Latte:
    def __init__(self):
        self.water = 100
        self.milk = 50
        self.coffee = 76
        self.money = 200

class Cappuccino:
    def __init__(self):
        self.water = 200
        self.milk = 100
        self.coffee = 160
        self.money = 400

class Report:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 220
        self.money = 0

def is_sufficient(beverage, report):
    return beverage.water <= report.water and beverage.coffee <= report.coffee and beverage.milk <= report.milk

def short(beverage, report):
    report.water -= beverage.water
    report.milk -= beverage.milk
    report.coffee -= beverage.coffee
    report.money += beverage.money

def display(report):
    print(f"Water: {report.water}ml")
    print(f"Milk: {report.milk}ml")
    print(f"Coffee: {report.coffee}g")
    print(f"Money: ${report.money}")

def money(beverage):
    amt = int(input("Enter the Money: "))
    if amt < beverage.money:
        print("Not Sufficient Amount. Your Money Has Been Refunded.")
    elif amt > beverage.money:
        change = amt - beverage.money
        print(f"Your Change: ${change}")

def machine():
    while True:
        latte = Latte()
        cappuccino = Cappuccino()
        report = Report()

        while True:
            user_input = input("What would you like to have? (Type 'L' for Latte, 'C' for Cappuccino, 'Report' for resource report, 'Restart' to restart, or 'Exit' to exit): ").lower()

            if user_input == "l":
                game(latte, report)
            elif user_input == "c":
                game(cappuccino, report)
            elif user_input == "report":
                display(report)
            elif user_input == "exit":
                return
            elif user_input == "restart":
                break
            else:
                print("Invalid input. Please choose 'L', 'C', 'Report', 'Restart', or 'Exit'.")

def game(beverage, report):
    if is_sufficient(beverage, report):
        display(beverage)
        money(beverage)
        short(beverage, report)
    else:
        print("Not Sufficient Resources")
        display(report)

machine()
