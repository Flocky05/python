/* The meaing of score refers to type of data like number and string or other things */
let score: number | string | boolean = 43;
score = "two";
console.log(score);

/* Display tpye of input */
function DisplyType(code: number | string | boolean) {
  if (typeof code === "number") {
    console.log("This is number type");
  } else if (typeof code === "string") {
    console.log("This is stirng type");
  } else if (typeof code === "boolean") {
    console.log("This is boolean type");
  } else {
    console.log("This unknown type data");
  }
}

DisplyType(true);
