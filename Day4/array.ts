let fruites: string[] = ["Mango", "Apple", "Banana", "Orange"];
fruites.push("Tomato");
//Here must every element will be string type other ways its gonna be show errors
console.log(fruites);
fruites.pop();
console.log(fruites);

/* If the array will be numbered type element , you can not added other type elements so you have to cearfull about the type of elements */

let number: number[] = [1, 56, 45, 89, 33, 45, 63, 61];
number.push(20);
console.log(number.sort());
//slice function is used for which number you inputed , after that number will printed Extracts a section of the array and returns the new array
let number2: number[] = [24, 45, 6, 2, 656, 9, 8, 32, 49];
console.log(number2.slice(3));

//
