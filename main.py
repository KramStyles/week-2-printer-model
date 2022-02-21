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

    def __init__(self):
        print(logo)
        self.print_type = input('What format would you like? ( coloured or greyscale ): ')
        self.pages = int(input('Enter Number of Pages to Print! '))
        # self.coin_type = input('Enter Cointype', 'Hey: ')
        # self.coins = input('Number of Coins: ')
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
            user_coins = input(f'Your Transaction would cost ${self.total}. Enter Amount you would pay: ')
            print(user_coins)
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
    job = Printer()