#!/usr/bin/node
// Script that computes and prints a factorial
let factorial = function (num) {
  let list = [];
  if (!num || isNaN(Number(num))) {
    return (1);
  } else if (list[num] > 0) {
    return (list[num]);
  }
  return (list[num] = factorial(num - 1) * num);
};

let result = factorial(process.argv[2]);
console.log(result);
