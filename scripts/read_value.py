from brownie import SimpleStorage,accounts,config

def read_contract():
    simple_storage = SimpleStorage[-1]

    #go take index one less then the length
    #ABI
    #Address
    print(simple_storage.retrive())
    


def main():
    read_contract()