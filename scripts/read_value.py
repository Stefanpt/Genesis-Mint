from brownie import Payments, GenesisBoulevard
from scripts.helpful_scripts import get_account

def read_contact():
    payments = Payments[-1]

    print(payments.totalShares())



def main():
    read_contact()