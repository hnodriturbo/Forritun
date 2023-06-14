/* var car = {
    make: 'bmw',
    model: '745i',
    year: 2010,

    // þessi function kallast method útaf þau eru inn í object
    getPrice: function() {
        //Perform some calc
        return 5000;
    },
    printDescription: function() {
        console.log(this.make + ' ' + this.model + ' ' + this.year);
    }
}

car.printDescription(); */

/* function first() {
    return this;
}

console.log(first() === global); */
/* 
function second() {
    'use strict';

    return this;
}


console.log(second() === global);
console.log(second() === undefined); */

let myObject = { value: 'My Object'};

// value is set on the global object
global.value = 'Global object';

function third(name) {
    return this.value + name;
}
console.log(third());

console.log(third.call(myObject, 'bob'))
console.log(third.apply(myObject))

// Hangman Game
const readline = require("readline");

const wordList = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape"]; // Array of words to choose from

let selectedWord = ""; // The word to be guessed
let guessedLetters = []; // Array to store guessed letters
let remainingGuesses = 6; // Number of remaining guesses

// Function to select a random word from the word list
function selectWord() {
  const randomIndex = Math.floor(Math.random() * wordList.length);
  selectedWord = wordList[randomIndex];
}

// Function to initialize the game
function initializeGame() {
  selectWord();
  guessedLetters = [];
  remainingGuesses = 6;
  updateDisplay();
}

// Function to update the display
function updateDisplay() {
  // Display the word with correctly guessed letters and underscores for unknown letters
  let displayWord = "";
  for (let i = 0; i < selectedWord.length; i++) {
    if (guessedLetters.includes(selectedWord[i])) {
      displayWord += selectedWord[i];
    } else {
      displayWord += "_";
    }
    displayWord += " ";
  }
  console.log("Word: " + displayWord);
  console.log("Guessed Letters: " + guessedLetters.join(", "));
  console.log("Remaining Guesses: " + remainingGuesses);
}

// Function to handle a guessed letter
function handleGuess(letter) {
  // Check if the letter has already been guessed
  if (guessedLetters.includes(letter)) {
    console.log("You've already guessed that letter!");
    return;
  }
  
  // Add the guessed letter to the array of guessed letters
  guessedLetters.push(letter);
  
  // Check if the guessed letter is in the selected word
  if (selectedWord.includes(letter)) {
    console.log("Correct guess!");
  } else {
    console.log("Wrong guess!");
    remainingGuesses--;
  }
  
  // Check if the game has been won or lost
  if (remainingGuesses === 0) {
    console.log("You lost! The word was: " + selectedWord);
    initializeGame();
  } else if (!displayWord.includes("_")) {
    console.log("Congratulations! You won!");
    initializeGame();
  } else {
    updateDisplay();
  }
}

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to handle user input
function handleUserInput() {
  rl.question("Enter a letter: ", function(answer) {
    handleGuess(answer.toLowerCase());
    handleUserInput();
  });
}

// Initialize the game
initializeGame();
handleUserInput();
