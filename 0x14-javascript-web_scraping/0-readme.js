#!/usr/bin/node
// Script that reads and prints the content of a file
let fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
