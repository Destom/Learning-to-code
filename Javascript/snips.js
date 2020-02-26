//single line comment

/* multi
line comment
*/

// "\" is the escape charater
a = "5"
parseInt(a); //will turn a to a string you need to store it as a vairable if you want to reuse

a= 5.tostring(/*anything in here will be the base number when converting to a sting*/); //will convert to a string

prompt('this will show a question you type to answer')

var name = 'destom';
console.log('Welcome ' + name);
console.log(typeof name); //view variable type

console.log("this will show up in the console")

alert('this is a string');

document.body.innerHTML = "hello world";

//an if statment, this can be nested
/*  function opperators
opperators in JS
== will check if the items look the same 6 = "6", === will also check if they are  the same class  so 6! = "6"

&& is the and opperator
|| is the or opperator
! at the beginning of a condition it will invert the results.

Falsy values (values assumed to be false) everything else is assumed to be true.
null
false
0
'' (any empty string)
undefined
*/
save = prompt("save?")
if (save=="yes") {
  alert('hello you chose to save')
}else if (save=="no") {
  alert('aww, ok I won\'t save :(')
}else {
  alert('The answer needed to be in the form of yes/no :(')
};

console.log("string".length)

//the switch statment (used to shorten if/else if blocks)
var x = parseInt(prompt('give me a number'))
switch (x){
  case 5:
    console.log('this is the magic number')
    break;
  case 6:
    console.log('your value is too big')
    break;
  case 4:
    console.log('your value is too small... she cried')
    break
  default:
    console.log('this is nowhere near the magic number')
    break
}

//magic number game with guess
magicNumber = Math.ceil(Math.random() *5)
console.log(magicNumber)
number = parseInt(prompt('please guess a number between 1 and 5'))
if (number== magicNumber){
  console.log('woo you guessed it ')
}
else {
  console.log('oh well looks like you have to play again')
};

//biggest number
number1 = prompt('give me the first number')
number2 = prompt('give me the second number')
number3 = prompt('give me the third number')
function biggestNumber(x,y){
    if (x > y)
    {
      return x
    }
    else{
      return y
    }
  }
biggestResult = biggestNumber(number1,number2)
biggestResult = biggestNumber(biggestResult,number3)
console.log(biggestResult)

// ++ or -- will add or remove one respectivly

for (var i = 1 ; i < 10 ; i++ ){
  console.log(i)
  }

  i=0
  while ( i <= 10){ //while loop runs only while condition is true
    console.log(i);
    i++;
  }

//break jumps out of a loop and continue will not run a single itteration.
