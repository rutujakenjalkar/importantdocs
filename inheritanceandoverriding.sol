// SPDX-License-Identifier: MIT
pragma solidity 0.8.30; //This is the comment

import {SimpleStorage} from "./SimpleStorage.sol";

contract AddFiveStorage is SimpleStorage{
   
   function store(uint256 _newNumber) public override {
        myfavoriteNumber=_newNumber+5;
   }

}
