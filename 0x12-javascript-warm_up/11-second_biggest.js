#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments

let list = [];
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (Number(process.argv[i])) {
      list.push(process.argv[i]);
    }
  }
  let sorted = list.sort().reverse();
  console.log(sorted[1]);
}
