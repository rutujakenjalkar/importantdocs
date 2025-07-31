//SPDX-License-Indentifier:MIT

// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

import "./SimpleStorage.sol";

contract StorageFactory{


    //type visibilty name;

    SimpleStorage[] public listsimpleStorage;
    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage=new SimpleStorage();
        listsimpleStorage.push(simpleStorage);
    }
    //How to call contract functions of a particular contract
    function sfStore(uint256 _simpleStorageIndex,uint256 _newSimpleStorageNumber) public {
        //ABI-Application Binary Interface
        SimpleStorage mySimpleStorage=listsimpleStorage[_simpleStorageIndex];
        mySimpleStorage.store(_newSimpleStorageNumber);
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256){
        SimpleStorage mySimpleStorage=listsimpleStorage[_simpleStorageIndex];
        return mySimpleStorage.retrieve();
    }

}
