from brownie import GenesisBoulevard as Collection
from scripts.helpful_scripts import get_account

def deploy_collection():
    payments_contract = "0xC7513655fdc79E078e8877E266cBF27E43e27386"
    account = get_account()

    collection = Collection.deploy(payments_contract, {'from': account}, publish_source=True) #* Remember to set verfication here when deploying to outside network

    name = collection.name()

    print(name)

def main():
    deploy_collection()