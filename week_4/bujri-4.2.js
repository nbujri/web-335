// title: bujri-4.2.js
// author: Ngi Bujri
// date: april 9 2023
// description: queries with mongosh

// queries all documents in users
db.users.find();

// find user with an email of jbach@me.com
db.users.find({ email: "jbach@me.com" });

// find user with last name Mozart
db.users.find({ lastName: "Mozart" });

// find user with first name Richard
db.users.find({ firstName: "Richard" });

// find user with employeeId 1010
db.users.find({ employeeId: "1010" });
