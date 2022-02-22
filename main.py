# The entry point of your application
from data.data import FORMAT as print_format, resources
from assets.art import logo


class Printer():
    # off turns off the system
    # report prints out current system status

    resource = resources
    currency = {'Pennies': 0.01, 'Nickels': 0.05, 'Dimes': 0.10, 'Quarters': 0.25}

    def __init__(self):
        print(logo)
        self.print_type = input('What format would you like? ( coloured or greyscale ): ')
        self.pages = int(input('Enter Number of Pages to Print! '))
        self.process_price()


    def check_resources(self):
        materials = print_format[self.print_type]['materials']
        ink = self.pages * materials['ink']
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
                user_coins += int(input(f"Enter amount you want to pay in {currency}: ")) * Printer.currency[currency]
            return user_coins

    def check_transactions(self):
        if self.process_price:
            user_coins = self.process_price()
            if self.total > user_coins:
                print ("Sorry that’s not enough coins. Coins refunded")
            else:
                self.report()
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
    job = Printer()