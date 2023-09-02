# QuizShuffle

QuizShuffle is a command-line utility that takes a '.txt' file as input and creates a new '.txt' file with a specified number of randomly selected questions from the input file. Whether you're a teacher looking to generate random quizzes or a student studying for an exam, QuizShuffle makes the process easy and efficient.

## Table of Contents
- [Eli5](#eli5)
- [How to Run](#how-to-run)
- [License](#license)
- [Common Errors](#common-errors)
- [Support](#support)
- [Feedback](#feedback)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

## Eli5

Have you ever had a file containing several questions? Whether you are a teacher or a student, this program lets you enter the name of a text file and a number (n), and it will create a new .txt file containing n randomly selected questions for you.

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

## Support

For support or assistance, please contact us at help@int-n.info.

## Feedback

We value your feedback! If you have any suggestions or encounter issues while using QuizShuffle, please reach out to us at help@int-n.info.

## Acknowledgements

We would like to acknowledge the [CS50P](https://cs50.harvard.edu/python/2022/) course for inspiration and guidance in creating QuizShuffle.

## Author

QuizShuffle is developed and maintained by [@abikahs](https://www.github.com/abikahs). Feel free to visit the GitHub repository for updates and contributions.
