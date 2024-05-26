const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name:{
        type: String,
        required: "Name is required !"
    },
    cardno:{
        type: String,
        required: "Email is required !"
    },
    pin:{
        type : String,
        required: "Password is required !"
    }
    ,
    phone:{
        type : String,
        required: "Password is required !"
    }
    ,
    balance:{
        type : String,
        required: "Password is required !"
    },
    accounttype:{
        type : String,
        required: "Password is required !"
    }
    },
    {
        timestamps: true,
    });

    module.exports = mongoose.model("User",userSchema);