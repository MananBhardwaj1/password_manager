
caeser = {

    "A": "N",

    "B": "O",

    "C": "P",

    "D": "Q",

    "E": "R",

    "F": "S",

    "G": "T",

    "H": "U",

    "I": "V",

    "J": "W",

    "K": "X",

    "L": "Y",

    "M": "Z",

    "N": "A",

    "O": "B",

    "P": "C",

    "Q": "D",

    "R": "E",

    "S": "F",

    "T": "G",

    "U": "H",

    "V": "I",

    "W": "J",

    "X": "K",

    "Y": "L",

    "Z": "M",

    "a": "n",

    "b": "o",

    "c": "p",

    "d": "q",

    "e": "r",

    "f": "s",

    "g": "t",

    "h": "u",

    "i": "v",

    "j": "w",

    "k": "x",

    "l": "y",

    "m": "z",

    "n": "a",

    "o": "b",

    "p": "c",

    "q": "d",

    "r": "e",

    "s": "f",

    "t": "g",

    "u": "h",

    "v": "i",

    "w": "j",

    "x": "k",

    "y": "l",

    "z": "m",

    "!": "=",

    "@": "+",

    "#": "-",

    "$": "_",

    "%": ")",

    "^": "(",

    "&": "*",

    "*": "&",

    "(": "^",

    ")": "%",

    "_": "$",

    "-": "#",

    "+": "@",

    "=": "!",

    ".": ".",

    "1": "7",

    "2": "3",

    "3": "9",

    "4": "6",

    "5": "4",

    "6": "2",

    "7": "1",

    "8": "0",

    "9": "5",

    "0": "8",

    " ": " "

}

















def coder(line):

    text = ""

    for i in line:

        word = caeser[i]

        text = text + word

    return text





def add():

    name = input("Account name: ")

    pwd = input("Password: ")

    with open("password.txt", "a") as file:

        file.write(coder(name) + "|" + coder(pwd) + "\n")



def view():

    with open("password.txt", "r") as file:

        for line in file.readlines():

            data = line.rstrip()

            user, passw = data.split("|")

            print("User:" , coder(user) , ", Password: ", coder(passw))



mode = ""



while mode != "add" and mode != "view" or mode != "1" and mode != "2":

    mode = input("Would you like to add new password or view exiting ones \n1. add \n2. view \n3. quit: \n: ").lower()



    if mode == "quit" or mode == "3":

        exit()

    

    elif mode == "add" or mode == "1":

        add()



    elif mode == "view" or mode == "2":

        view()

