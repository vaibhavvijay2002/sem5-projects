const sha256 = require("js-sha256");

var pin= sha256("1111"+process.env.SALT);
console.log(pin);