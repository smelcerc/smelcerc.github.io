'''
File: credit_card.py
Author: Christopher Smelcer
W04 Prepare: Checkpoint B
'''

from address import Address

class CreditCard:
    """ Contains a credit card that has two addressess"""
    def __init__(self):
        self.name = ""
        self.number = ""
        self.mailing_address = Address()
        self.billing_address = Address()

    def display(self):
        print(self.name)
        print(self.number)
      
        print("Mailing Address:")
        self.mailing_address.display()

        print("Billing Address:")
        self.billing_address.display()