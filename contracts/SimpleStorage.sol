//"SPDX-License-Identifier: MIT"

pragma solidity ^0.6.0;




contract SimpleStorage {

    uint256 favouriteNumber;
    bool favouriteBool;


    struct People {
        uint256 favouriteNumber;
        string name;
    }

    People[] public people;
    mapping(string=> uint256) public nameTOFavouriteNumber;


    function  store(uint256 _favouriteNumber) public returns(uint256){
        favouriteNumber = _favouriteNumber;
        return favouriteNumber;
    }

    function retrive() public view returns(uint256){
        return favouriteNumber;
    }

    function addPerson(string memory _name,uint256 _favouriteNumber) public {
        people.push(People({favouriteNumber:_favouriteNumber,name: _name}));
        nameTOFavouriteNumber[_name] = _favouriteNumber;
    }


}