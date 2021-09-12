// GUESSING GAME



// Getting the range, then checking if the user gave a valid number
let maximum = parseInt(prompt("Enter your max num"));
while (!maximum) {
    if (maximum === 0) {
        maximum = parseInt(prompt("Enter a number greater than 0"));
        continue
    }
    maximum = parseInt(prompt("Enter a valid number"));
}

// Getting guesses, then checking if they are lower or higher than the original number, then ask them again, until they guess it
const target_num = Math.floor(Math.random() * maximum) + 1;
let guess = prompt("Enter your first guess: ");
let attempts = 1;
let ending = "st";
while (parseInt(guess) !== target_num) {
    attempts += 1;
    // I may quit the game here
    if (guess === "q") {
        break
    }
    // Some useless thing
    if (attempts === 2) {
        ending = "nd";
    } else {
        ending = "th";
    }
    if (guess > target_num) {
        guess = prompt("Lower");
    } else {
        guess = prompt("Higher");
    }
}
if (guess === "q") {
    console.log("I'm sad to see you go :((")
} else {
    console.log(`You got it RIIIGHT!! It's ${target_num} indeed! You got it after the ${attempts + ending} attempt `)
}
