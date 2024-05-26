const mongoose = require("mongoose");
const User = mongoose.model("User");
const sha256 = require("js-sha256");
const jwt = require('jsonwebtoken');


exports.login = async (req, res) => {
    const {cardno , pin} = req.body;
    const user = await User.findOne({
        cardno,
        pin: sha256(pin+process.env.SALT),
    });

    if(!user) throw "Invalid Card Number And Pin !";
    
     
    res.json({
        message: "User logged in successfully !",
    });

};

exports.checkBalance = async (req, res) => {
    const {cardno} = req.body;
    const user = await User.findOne({
        cardno
    });

    if(!user) throw "User Does Not Exist !";
     
    res.json({
        message: "fetched User Balance !",
        account: user
    });

};

exports.accountInfo = async (req, res) => {
    const {cardno} = req.body;
    // fetching in DB
    const user = await User.findOne({
        cardno
    });

    if(!user) throw "User Does Not Exist !";
     
    res.json({
        message: "Account Info has been fetched",
        account: user // this user is JSON Object  which contains user name, pin, balance, card no, account type, phone number can be extracted in front end
    });

};

exports.withdrawMoney = async (req, res) => {

    const {cardno,amount} = req.body;
    const user = await User.findOne({
        cardno
    });

    if(!user) throw "User Does Not Exist !";


        if(Number(amount)>Number(user.balance)){
            res.json({
                message: "Insufficient Funds !"
            });
        }
        else{

            balance = Number(user.balance)
            balance = balance-Number(amount)
            var myquery = { cardno: cardno };
            var newvalues = { $set: {balance: balance} };

            User.updateOne(myquery, newvalues,(err, res)=>{
            if (err) throw err;
            console.log("1 document updated");
            
        });

            res.json({
            message: "Transaction Successfull !",
        });

        };
        
    };


exports.depositMoney = async (req, res) => {
    const {cardno ,amount} = req.body;
    const user = await User.findOne({
        cardno,
    });
    if(!user) throw "User Does Not Exist !";
    
   
        if(amount>10000){
            res.json({
                message: "You Can Only Deposit Up To 10000 RS Only !"
            });
        }
        else{
            balance = Number(user.balance)
            balance = balance+Number(amount)
           
            var myquery = { cardno: cardno };
            var newvalues = { $set: {balance: balance} };
            User.updateOne(myquery, newvalues,(err, res)=>{
            if (err) throw err;
            console.log("1 document updated");
            });
            res.json({
            message: "Transaction Successfull !",
        });

        }
        
    
};

exports.changePin = async (req, res) => {
    const {cardno ,oldpin, newpin} = req.body;
    const user = await User.findOne({
        cardno
    });

    if(!user) throw "Invalid Pin !";

    Noldpin = sha256(oldpin+process.env.SALT);
    Nnewpin = sha256(newpin+process.env.SALT);
    

    if(Noldpin==user.pin){
        var myquery = { cardno: cardno };
    var newvalues = { $set: {pin: Nnewpin} };
    User.updateOne(myquery, newvalues,(err, res)=>{
    if (err) throw err;
    console.log("1 document updated");
    });
     
    res.json({
        message: "Pin Changed successfully !",
    });
    }
    else{
        throw "Wrong Old Pin !";
    }
    

};

exports.changePhone = async (req, res) => {
    const {cardno ,oldphone, newphone} = req.body;
    const user = await User.findOne({
        cardno
    });

    if(!user) throw "User Does Not Exists !";
    
    if(oldphone==user.phone){

    var myquery = { cardno: cardno };
    var newvalues = { $set: {phone: newphone } };
    User.updateOne(myquery, newvalues,(err, res)=>{
    if (err) throw err;
    console.log("1 document updated");
    });

    res.json({
        message: "Changed Phone Number Successfully !"
    });

    }
    else
    {
        throw "Invalid Old Phone Number !";
    }
    
};

