
var mysql = require('mysql');
var connection = mysql.createConnection({
    host    :'localhost',
    port : 1234,
    user : 'root',
    password : '123456',
    database:'sh',
});

connection.connect();
connection.end();
