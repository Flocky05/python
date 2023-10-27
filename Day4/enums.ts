/* Some time u have to need more types in a common environment that time you can you use it */
/* Enums are a feature added to JavaScript by TypeScript which allows for describing a value which could be one of a set of possible named constants. Unlike most TypeScript features, this is not a type-level addition to JavaScript but something added to the language and runtime. */
enum setChoice {
  AISLE = 27,
  MIDDLE,
  WINDOW,
  FOURTH,
}

const seat = setChoice.MIDDLE;
console.log(seat);
