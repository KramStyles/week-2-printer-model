# The entry point of your application
from data.data import FORMAT as format, resources


class Printer():
    # off turns off the system
    # report prints out current system status
    def __init__(self, pages, coins):
        self.pages = pages
        self.coins = coins

    def turn_off(self):
        print("Bye!")
        SystemExit()

    def checkTransactions(self):
        pass

class GreyPrinter(Printer):
    pass

class ColoredPrinter(Printer):
    pass

# resources['ink'] = 300

job1 = GreyPrinter(100, 20)
job1.turn_off()