var userInput;
var last2Dig = userInput % 100;
var lastDig = userInput % 10;
if (last2Dig >=11&&last2Dig<=13) {
    console.log(userInput + "th");
}
else if (lastDig == 1) {
    console.log(userInput + "st");
}
else if (lastDig == 2) {
    console.log(userInput + "nd");
}
else if (lastDig == 3) {
    console.log(userInput + "rd")
}
else {
    console.log(userInput + "th");
}