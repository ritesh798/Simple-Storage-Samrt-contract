from brownie import accounts,config,SimpleStorage,network
import time


def deploy_simple_storage():
    account = get_account()
    #print(account)
    #account = accounts.add(config["wallets"]["from_keys"])
    simple_storage = SimpleStorage.deploy({"from":account})
    time.sleep(1)
    stored_value = simple_storage.retrive()
    print(stored_value)
    transaction = simple_storage.store(15,{"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrive()
    print(updated_stored_value)

def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']["from_keys"])
def main():
  deploy_simple_storage()