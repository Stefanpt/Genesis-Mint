from brownie import Payments
from scripts.helpful_scripts import get_account

def deploy_payments():
    addresses = [
        "0xe8D09D8a584c5aEeA31F6CCb125263f20edF3872"
    ]
    shares = [
        "100"
    ]
    account = get_account()
    payment = Payments.deploy(addresses, shares, {'from': account}, publish_source=True) #* Remember to set verfication here when deploying to outside network
    
    address_shares = payment.shares(addresses[0])

    print(address_shares)

def main():
    deploy_payments()