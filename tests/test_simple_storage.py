from brownie import SimpleStorage,accounts

def test_deploy():
    #arrange
    account = accounts[0]

    #ACT
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = simple_storage.retrive()
    expected = 0
    #Assert
    assert starting_value == expected

def test_updating_storage():
    #Arrange
    account  = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    #Act
    expected = 15
    simple_storage.store(expected,{"from":account})

    #Assert
    assert expected == simple_storage.retrive()

