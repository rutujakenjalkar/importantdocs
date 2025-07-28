// SPDX-License-Identifier: MIT
pragma solidity 0.8.30; //This is the comment
//First contract
contract SimpleStorage{
    // Favorite number is zero if no value given
    uint256 public myfavoriteNumber;//default 0
    

    //Class
    struct Person{
        uint favoritenumber;
        string name;
    }

    //Object Creation
    // Person public myfriend=Person({name:"Rahul",favoritenumber:3});
    // Person public myfriend2=Person({name:"Rutuja",favoritenumber:4});

    Person[] public people;// dynamic arrays






    function store(uint256 _favoriteNumber) public {
        myfavoriteNumber=_favoriteNumber;
         
    }

    function retrieve () public view returns(uint256){
        return myfavoriteNumber;
    }
   


    function addPerson(uint256 _favoritenumber,string memory _name) public {
        people.push(Person(_favoritenumber,_name));
    }
    
}
