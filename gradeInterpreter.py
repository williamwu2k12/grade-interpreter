grades = open("grades.txt")
letters = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "P": 0, "NP": 0}
numbers = {4.0: "A", 3.7: "A-", 3.3: "B+", 3.0: "B", 2.7: "B-", 2.3: "C+", 2.0: "C", 1.7: "C-", 0: "P"}

# gpas, where first item in array is the total points (with unit multipliers), and second is the total units
total = [0.0, 0]
tech = [0.0, 0]

index = 0
classes = []

class data:
    def __init__(self, title, subtitle, units, grade, tech):
        self.title = title
        self.subtitle = subtitle
        self.units = units
        self.grade = grade
        self.tech = tech

def processClass(string):
    i = 2
    while (string[i] != ":"):
        i += 1
    title = string[2:i]
    subtitle = string[(i + 2):(len(string) - 1)]
    classes.append(data(title, subtitle, 0, 0.0, False))

def processUnits(string):
    classes[index].units = int(string[7:(len(string) - 1)])

def processGrade(string):
    result = 0;
    letter = string[7:(len(string) - 1)]
    result = letters[letter]
    classes[index].grade = result

def processTech(string):
    global index
    string = string[6:(len(string) - 1)]
    if (string == "yes"):
        classes[index].tech = True
    if (string == "no"):
        classes[index].tech = False
    processEnd()
    index += 1

def processEnd():
    global index
    if (classes[index].grade != 0):
        total[0] += classes[index].grade * classes[index].units
        total[1] += classes[index].units
        if (classes[index].tech):
            tech[0] += classes[index].grade * classes[index].units
            tech[1] += classes[index].units

def processFile(text):
    for line in text:
        if (line[0] == "\n" or line[0] == "#"):
            continue
        if (line[0] == "-"):
            processClass(line)
        if (line[0:5] == "units"):
            processUnits(line)
        if (line[0:5] == "grade"):
            processGrade(line)
        if (line[0:4] == "tech"):
            processTech(line)
processFile(grades)



def processInput():
    text = input("-> ")
    if (text == "classes"):
        for obj in classes:
            print(obj.title)
            print(obj.subtitle)
            print(str(obj.units) + " : " + str(numbers[obj.grade]))
    elif (text == "gpa"):
        print("total: " + str(total[0] / total[1]) + " units: " + str(total[1]))
        print("tech: " + str(tech[0] / tech[1]) + " units: " + str(tech[1]))
    elif (text == "help"):
        print("commands: 'classes', 'gpa', 'exit/end/quit'")
    elif (text == "exit" or text == "end" or text == "quit"):
        return
    else:
        print("invalid command, please try again")
    processInput()
processInput()
