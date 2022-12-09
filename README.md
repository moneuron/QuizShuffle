
# QuizShuffle
Gets a '.txt' file name as a command line argument.
Prompts for a '.txt' file name and a number.
Writes a .txt file with (n = number) of questions shuffled.

## Eli5

Have you ever had a file containing several questions?
Whether you are a teacher or a student, this program lets you enter the name of a text file, and a number(n), and will create a .txt file containing n questions randomly picked for you.
## How to run

To run the program:
```bash
  python main.py -n "filename.txt"
```

Enter the number of questions you want: (e.g. 12)
```bash
  Number of Questions: 12
```

Enter a name to save your file: (e.g. Output.txt)
```bash
  File Name: Output.txt
```

You should see the following output:
```bash
  Done! Output.txt is created.
```
## Roadmap

- Additional file format support

- Add more features


## License

open-source license


## Common Errors

#### Running the program without providing a command-line argument:
```bash
usage: project.py -n "filename.txt"
```

#### Running the program and providing an Invalid command-line argument:
```bash
Invalid entry
```

#### Running the program and providing a command-line argument that does not exist:
```bash
Could not read filename.txt
```

#### Running the program and providing non-int input for 'Number of Questions':
```bash
'Number of Questions' should be an int!
```

#### Running the program and entering a number greater than the amount of lines in -n "filename.txt":
```bash
Not enough questions in filename.txt
```

#### Running the program and providing an input that does not end with '.txt' for 'File Name' : 
```bash
'File Name' should end with .txt
```
## Support

For support, email sirshakiba@outlook.com.


## Feedback

If you have any feedback, please reach out to me at sirshakiba@outlook.com


## Acknowledgements

 - [CS50P](https://cs50.harvard.edu/python/2022/)


## Author

- [@abikahs](https://www.github.com/abikahs)

