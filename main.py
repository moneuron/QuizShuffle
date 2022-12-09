import sys
import argparse
import random


def main():
    inp = get(sys.argv[1:])
    allq = open_txt(inp)
    try:
        num = int(input("Number of Questions: "))
    except:
        sys.exit("'Number of Questions' should be an int!")
    if num > len(allq):
        sys.exit(f"Not enough questions in {inp}")
    output = input("File Name: ")
    if output.endswith(".txt"):
        pass
    else:
        sys.exit("'File Name' should end with .txt")

    randomq = random_pick(num, allq)
    write_txt(randomq, output)


def get(addy):
    """
    Get the file name or path. (.txt)
    :param: system.argv[1:]
    :type param: list
    :ValueError: if the entry doesn't end with .txt
    :return: the file name
    :rtpe: str
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n")
    args = parser.parse_args(addy)
    if args.n == None:
        raise ValueError("usage: project.py [-h] [-n N]")
    if args.n.endswith(".txt"):
        return args.n
    else:
        raise ValueError("Invalid entry")


def open_txt(inp):
    """
    Opens .txt file
    :param: the file name
    :type param: str
    :ValueError: if the file does not exist
    :return: a list of dictionaries where keys are numbers and values are questions
    :rtpe: list
    """
    try:
        with open(inp, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise ValueError(f"Could not read {inp}")
    else:
        questions = []
        for i, question in enumerate(lines):
            questions.append({"N": i, "Q": question.strip()})
        return questions


def random_pick(n, questions):
    """
    Picks n random questions from a list
    :param: n, a list of questions
    :type param: n: int , questions: list
    :return: a set of random questions
    :rtpe: set
    """
    random_questions = set()
    while len(random_questions) < n:
        r = random.randint(0, len(questions) - 1)
        random_questions.add(questions[r]["Q"])
    return random_questions


def write_txt(random_questions, output):
    """
    Writes a .txt file
    :param: a set of questions, file's name
    :type param: random_questions: set , output: str
    """
    with open(output, "w") as file:
        for line in random_questions:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
