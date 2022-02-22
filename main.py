# The entry point of your application
from data.data import FORMAT as print_format, resources
from assets.art import logo


class Printer:
    # off turns off the system
    # report prints out current system status

    resource = resources
    currency = {'Pennies': 0.01, 'Nickels': 0.05, 'Dimes': 0.10, 'Quarters': 0.25}

    def __init__(self):
        print(logo)
        print("What format would you like? ( coloured or greyscale ). ")
        self.print_type = input("Type g for Greyscale and c for Coloured: ")
        self.pages = int(input('Enter Number of Pages to Print! '))
        self.response = 0
        self.run_transactions()

    def verify_input(self, value):
        if value.lower() == 'off': self.turn_off()
        elif value.lower() == 'report': self.report()
        else: print("Unknown Input")
        return True

    def check_resources(self):
        self.materials = print_format[self.print_type]['materials']
        ink = self.pages * self.materials['ink']
        if self.pages > Printer.resource['paper']:
            print("Sorry, there's not enough paper")
        elif ink > Printer.resource['ink']:
            print("Sorry, there is not enough ink")
        else:
            return True

    def process_price(self):
        if self.check_resources():
            price = print_format[self.print_type]['price']
            self.total = self.pages * price
            print(f'Your Transaction would cost ${self.total}. ')
            user_coins = 0
            for currency in Printer.currency:
                money = input(f"Enter amount you want to pay in {currency}: ")
                user_coins += (int(money) * Printer.currency[currency]) if money.isdigit() else self.verify_input(money)
            return user_coins

    def run_transactions(self):
        if self.process_price:
            user_coins = self.process_price()
            if self.total > user_coins:
                print("Sorry that’s not enough coins. Coins refunded")
            else:
                Printer.resource['ink'] -= (self.materials['ink'] * self.pages)
                Printer.resource['paper'] -= self.pages
                Printer.resource['profit'] += self.total
                if user_coins > self.total:
                    print('This is your change:', user_coins - self.total)
                self.thank_you()

    @classmethod
    def turn_off(cls):
        print("Bye!")
        exit()

    @classmethod
    def report(cls):
        print(f"\nPaper: {resources['paper']}pc")
        print(f"Ink: {resources['ink']}ml")
        print(f"Profit: ${resources['profit']}\n")

    @staticmethod
    def thank_you():
        print("Here's your project")
        print("Thank you for using our services. We hope to see you soon")


if __name__ == '__main__':
    job2 = Printer()
