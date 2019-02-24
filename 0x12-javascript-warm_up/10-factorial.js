#!/usr/bin/node
// Script that computes and prints a factorial
let factorial = function (num) {
  return num ? num * factorial(num - 1): 1;
};

let result = factorial(process.argv[2]);
console.log(result);
