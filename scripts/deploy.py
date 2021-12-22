from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # account = accounts.load("SolidityCourse")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)


def main():
    deploy_simple_storage()
