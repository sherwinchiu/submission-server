## Question 1

### Number comparison

User will ask for two different numbers. Compare the two numbers, and state whether the numbers are equal, less than, or greater than.

```
What is the first number? 5
What is the second number? 2

5 is greater than 2

What is the first number? 3
What is the second number? 3

3 is equal to 3

What is the first number? 15
What is the second number? 1

15 is less than 1

```

## Question 2

### Calculator

User will create a calculator that takes in two numbers, then can either add, subtract, multiply or divide (+, -, \*, /). The first number inputted will be the first number, and the second number is the one after the operation.

```
What is the first number? 3
What is the second number? 5
What operation do you want to do? *
The output is 15
```

## Question 3

### Grade Scheme

User will ask for what percent grade you got, and translate it to a letter grade and print out the corresponding text.

A: 80 - 100
B: 70 - 79
C: 60 - 69
D: 50 - 59
F: 0 - 50

```
What was your grade? 90
Congrats on getting an A!

What was your grade? 70
Good job on getting a B!

What was your grade? 68
You got a C, work a bit harder!

What was your grade? 58
You got a D.

What was your grade? 34
Unfortunately, you got a F. Try again, you can do it!
```

## Question 4

### Working with ASCII

User will ask for a character. Then, output if the character is a number, a special character, a lowercase letter or uppercase letter. You will have to use an ASCII table for this! You can worry about the decimal range of the ASCII table from 33 to 126, inclusive (meaning include 33 and 126).

```
What is your character? ?
That is a special character.

What is your character? 5
That is a number.

What is your character? A
That is an uppercase letter.

What is your character? d
That is a lowercase letter.
```

## Question 5

### Divisibility

User will ask for two numbers, and using the remainder operator, figure out if the first number is divisible by the second. Print out the corresponding text.

```
What is the first number? 5
What is the second number? 2
5 is not divisible by 2.

What is the first number? 33
What is the second number? 11
33 is divisible by 11.
```

## Question 6

### Number Guesser

User will import **cstdlib** to generate a random number from 1 to 100. A guessing game will occur where the user will guess a number, and the program will tell them if the number is higher or lower. This will continue until the correct number is guessed

```
What number do you guess? 50
The number is higher.
What number do you guess? 75.
The number is lower.
What number do you guess? 62
The number is higher.
What number do you guess? 65
That is the correct number!
```

## Question 7

### Factorial

User will input a number and calculate the factorial of the number. The factorial is simply calculated by multiplying every number from 1 to the number inputted. For example, the factorial of 5 is (1 \* 2 \* 3 \* 4 \* 5) = 120. Try to implement this with both while loops and for loops, and note which one was easier for you.

```
What number do you want to factorial? 5
120

What number do you want to factorial? 3
6
```

## Question 8

### Reverse a number

User will input an integer that is big. The program will print out the reverse of that number. (Hint: Modulus needed)

```
What number do you want to reverse? 5123514
4153215
```

## Question 9

### Rectangle

User will input an width and height. Draw a rectangle made out of astricks with these parameters. Use while loops or for loops.

```
What is the width of the rectangle? 5
What is the height of the rectangle? 4

*****
*****
*****
*****
```

## Question 10

### Fibonacci Sequence

Fibonacci sequence is a mathematical sequence that goes up by adding a number previous to the number you are on. For example, a Fibonacci sequence of 7 numbers is (1, 1, 2, 3, 5, 8, 13). 1 + 1 = 2, 2 + 3 = 5, 5 + 8 = 13, and so on. User will ask for how many numbers you want the sequence to go up to, and will be printed accordingly. Have the sequence of numbers only be seperated by spaces.

```
How many numbers of the sequence do you want to print? 10
1 1 2 3 5 8 13 21 34 55

```
