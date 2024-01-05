const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");


let [str1, str2] = input;

console.log(str1.length + str2.length);