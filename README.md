# QuizShuffle
##### by [Mo Shakiba](https://github.com/moneuron)

QuizShuffle is a command-line utility that takes a '.txt' file as input and creates a new '.txt' file with a specified number of randomly selected questions from the input file. Whether you're a teacher looking to generate random quizzes or a student studying for an exam, QuizShuffle makes the process easy and efficient.

---
## How to Run

To run the program, open your terminal and use the following command:

```
python main.py -n "filename.txt"
```

You'll be prompted to provide the following information:

1. Enter the number of questions you want (e.g., 12):
```
Number of Questions: 12
```

2. Enter a name to save your file (e.g., Output.txt):
```
File Name: Output.txt
```

After completing these steps, you should see the following output:

```
Done! Output.txt is created.
```

## License

QuizShuffle is released under an open-source license.

## Common Errors

Here are some common errors and their corresponding error messages:

#### Running the program without providing a command-line argument:
```
Usage: python main.py -n "filename.txt"
```

#### Running the program and providing an invalid command-line argument:
```
Invalid entry
```

#### Running the program and providing a command-line argument that does not exist:
```
Could not read filename.txt
```

#### Running the program and providing non-integer input for 'Number of Questions':
```
"Number of Questions" should be an integer!
```

#### Running the program and entering a number greater than the number of lines in "filename.txt":
```
Not enough questions in filename.txt
```

#### Running the program and providing an input that does not end with '.txt' for 'File Name':
```
"File Name" should end with .txt
```
