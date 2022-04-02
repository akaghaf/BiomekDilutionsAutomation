import csv
from os.path import exists


def set_source_well(file):
    # Brief: Convert csv into list to popluate the source well
    # param file: file we want to convert into list
    if exists(file):
        with open(file, newline='') as f:
            return(list(csv.reader(f))[0])
    else:
        return(None)

def set_dest_well(file):
    # Brief: Convert csv into list to popluate the dest well
    # param file: file we want to convert into list
    return(set_source_well(file))


def yes_or_no(question):
    # Brief: Used to ask a user a yes or no question
    # param question: question to ask the user
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

