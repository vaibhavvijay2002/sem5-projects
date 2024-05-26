require('dotenv').config();
const mongoose = require("mongoose");

//Cross-origin resource sharing (CORS)

require("cors");

// MongoDB connection
mongoose.connect(process.env.DB, { useNewUrlParser: true, useUnifiedTopology: true });
mongoose.connection.once('open', () => {
    console.log("MongoDB Connected!")
});

//DB models
require('./models/user');

// Server 
const app = require("./app");

const server = app.listen(8000, () => {
    console.log("Server is listning on port 8000")
});


