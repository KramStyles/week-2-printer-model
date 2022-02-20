# The entry point of your application
from cmath import log
from pip import main
from data.data import FORMAT as format, resources
from assets.art import logo

class Printer():
    # off turns off the system
    # report prints out current system status

    currency = {
        'Penny':0.01,
        'Nickel':0.05,
        'Dime':0.10,
        'Quarter':0.25
    }


    def __init__(self):
        self.pages = input('Enter Number of Pages to Print! ')
        self.type = input('Enter Cointype', 'Hey: ')
        self.coins = input('Number of Coins: ')

    def turn_off(self):
        print("Bye!")
        SystemExit()

    def checkTransactions(self):
        total = self.pages * self.coins

class GreyPrinter(Printer):
    pass

class ColoredPrinter(Printer):
    pass

# resources['ink'] = 300

# job1 = GreyPrinter()
# job2 = ColoredPrinter()
# job1.turn_off()

if __name__ == '__main__':
    print(logo)
    job1 = GreyPrinter()