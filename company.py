from data.data import FORMAT as print_format, resources
from assets.art import logo

print(logo)


class Printer:
    """
    The Class Model of a Printing machine that is able to print both in greyscale and coloured format depending on the
    user’s choice.
    output: str - Message giving replies to the user depending on choices made
    """

    resource = resources
    currency = {'Pennies': 0.01, 'Nickels': 0.05, 'Dimes': 0.10, 'Quarters': 0.25}

    def __init__(self):
        self.print_type = None
        self.pages = None
        self.response = 0

        self.turn_on()

    def turn_on(self):
        print("\n\nWhat format would you like? ( coloured or greyscale ). ")
        while self.print_type is None or str(self.print_type).isdigit():
            self.print_type = self.verify_input(input("Type g for Greyscale and c for Coloured: "))
        while self.pages is None or not str(self.pages).isdigit():
            self.pages = self.verify_input(input('Enter Number of Pages to Print! '))
        self.run_transactions()

    def verify_input(self, value):
        value = value.strip()
        if value.lower() == 'off': self.turn_off()
        elif value.lower() == 'g': return 'greyscale'
        elif value.lower() == 'c': return 'coloured'
        elif value.isdigit(): return int(value)
        elif value.lower() == 'report': self.report()
        else: print("Unknown Input. Please try again!")
        return None

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
                money = None
                while money is None or not str(money).isdigit():
                    money = self.verify_input(input(f"Enter amount you want to pay in {currency}: "))
                user_coins += money * Printer.currency[currency]
            return user_coins

    def run_transactions(self):
        user_coins = self.process_price()
        if user_coins:
            if self.total > user_coins:
                print("Sorry that’s not enough coins. Coins refunded")
            else:
                Printer.resource['ink'] -= (self.materials['ink'] * self.pages)
                Printer.resource['paper'] -= self.pages
                Printer.resource['profit'] += self.total
                if user_coins > self.total:
                    print(f'Here is ${user_coins - self.total} in change.')
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
        print("Thank you for using our services. We hope to see you soon.")