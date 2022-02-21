# The entry point of your application
from data.data import FORMAT as print_format, resources
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
        self.print_type = input('What format would you like? ( coloured or grayscale )')
        self.pages = input('Enter Number of Pages to Print! ')
        # self.coin_type = input('Enter Cointype', 'Hey: ')
        # self.coins = input('Number of Coins: ')
        self.check_resources()


    def check_resources(self):
        materials = print_format[self.print_type]['materials']
        print(self.pages)

    def process_price(self, pages):
        self.total = pages * Printer.prices[self.type]
        user_coins = input(f'Your Transaction would cost ${self.total}. Enter Amount you would pay')
        return user_coins

    def check_transactions(self):
        user_coins = self.process_price(self.pages)
        if self.total > user_coins:
            return "Sorry that’s not enough coins. Coins refunded"
        else:
            Printer.resource['ink'] -= (print_format[self.print_type]['materials']['ink'] * self.pages)
            Printer.resource['paper'] -= self.pages
            Printer.resource['profit'] += self.total
            if user_coins > self.total:
                print('This is your change:', user_coins - self.total)
            return True
    
    def thank_you(self):
        print("Here's your project")
        print("Thank you for using our services. We hope to see you soon")


    @classmethod
    def turn_off(self):
        print("Bye!")
        SystemExit()

    @classmethod
    def report(self):
        print(f"Paper: {resources['paper']}pc")
        print(f"Ink: {resources['ink']}ml")
        print(f"Profit: ${resources['profit']}")

    @staticmethod
    def handle_processes():
        print('hello')



if __name__ == '__main__':
    Printer.process_price('', 12)
