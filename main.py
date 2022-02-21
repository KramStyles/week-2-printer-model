# The entry point of your application
from data.data import FORMAT as format, resources
from assets.art import logo


class Printer():
    # off turns off the system
    # report prints out current system status

    resource = resources
    currency = {
        'Penny': 0.01,
        'Nickel': 0.05,
        'Dime': 0.10,
        'Quarter': 0.25
    }
    prices = {'coloured': 35, 'grayscale': 25}

    def __init__(self):
        self.type = input('What format would you like? ( coloured or grayscale )')
        self.pages = input('Enter Number of Pages to Print! ')
        self.type = input('Enter Cointype', 'Hey: ')
        self.coins = input('Number of Coins: ')

    def check_resources(self):
        pass

    def process_price(self, pages):
        self.total = pages * Printer.prices[self.type]
        user_coins = input(f'Your Transaction would cost ${self.total}. Enter Amount you would pay')
        return user_coins

    def check_transactions(self, ):
        user_coins = self.process_price(self.pages)
        if self.total > user_coins:
            
    @classmethod
    def turn_off(self):
        print("Bye!")
        SystemExit()

    @classmethod
    def report(self):
        print(f"Paper: {resources['paper']}pc")
        print(f"Ink: {resources['ink']}ml")
        print(f"Profit: ${resources['profit']}")


class GreyPrinter(Printer):
    pass


class ColoredPrinter(Printer):
    pass

# resources['ink'] = 300

# job1 = GreyPrinter()
# job2 = ColoredPrinter()
# job1.turn_off()


if __name__ == '__main__':
    Printer.process_price('', 12)
