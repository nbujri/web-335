/**
 * title: bujri-projections.js
 * author: ngi bujri
 * date: april 16 2023
 * description: assignment 5.2 - projections
 */

// add new user

db.users.insertOne({
  firstName: "Antonio",
  lastName: "Vivaldi",
  employeeId: "1013",
  email: "avivaldi@me.com",
  dateCreated: new Date(),
});

// update email to mozart@me.com
db.users.updateOne(
  { lastName: "Mozart" },
  {
    $set: { email: "mozart@me.com" },
  }
);

// find updated email
db.users.aggregate([{ $match: { email: "mozart@me.com" } }]);

// return all documents but only with firstName, lastName, and email
db.users.aggregate([
  {
    $project: {
      _id: 0,
      firstName: 1,
      lastName: 1,
      email: 1,
    },
  },
]);
