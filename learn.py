
TOPICS = {
    "Variables": {
        "concept": """A variable is just a name that stores a value.
We use it so we don't have to write the same value again and again.
In Python we create a variable by assigning a value to it.""",
        "example": """age = 18
name = "Aarjav"
age = 19

print(name)
print(age)""",
        "explanation": """First age becomes 18, then name stores text.
After that age is changed to 19. Python decides the type automatically.""",
        "points": """• Give meaningful names
• Can use letters, digits and underscore
• Cannot start with a digit
• No spaces allowed
• Python is case sensitive
• Don't use keywords as names"""
    },
    "Data Types": {
        "concept": """Data type tells what kind of value is stored.
Common ones: int (whole numbers), float (decimals),
str (text), bool (True/False), list, tuple, dict.""",
        "example": """age = 18
height = 5.8
name = "Aarjav"
passed = True

print(type(age))
print(type(height))
print(type(name))
print(type(passed))""",
        "explanation": """age is int, height is float, name is string
and passed is boolean. type() function shows the type.""",
        "points": """• int = whole numbers
• float = decimal numbers
• str = text
• bool = True or False
• list, tuple, dict are collections"""
    },
    "Input and Output": {
        "concept": """input() is used to take value from user.
print() is used to show output.
Together they make the program interactive.""",
        "example": """name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Next year you will be", age + 1)""",
        "explanation": """input() always gives string.
We use int() to convert it when we need a number.""",
        "points": """• input() takes input
• print() shows output
• input() returns string by default
• Use int() or float() for numbers
• Write clear prompts"""
    },
    "Operators": {
        "concept": """Operators are used to perform operations.
Arithmetic for calculation, comparison for comparing,
logical for combining conditions.""",
        "example": """a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)""",
        "explanation": """+ add, - subtract, * multiply, / divide
// floor division, % remainder, ** power.""",
        "points": """• Arithmetic: + - * / // % **
• Comparison: == != > < >= <=
• Logical: and or not
• = is assignment, == is comparison"""
    },
    "If-Else": {
        "concept": """if-else is used for decision making.
if checks a condition, elif checks another,
else is the last option.""",
        "example": """marks = int(input("Enter marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
else:
    print("Keep practicing")""",
        "explanation": """Python checks conditions from top.
Indentation is very important in Python.""",
        "points": """• Conditions give True or False
• Indentation matters a lot
• Use == for comparison
• elif for extra conditions
• else is optional"""
    },
    "For Loop": {
        "concept": """for loop is used when we know how many times
to repeat. range() is commonly used with it.""",
        "example": """for i in range(1, 6):
    print(i)

numbers = [10, 20, 30]
for number in numbers:
    print(number)""",
        "explanation": """range(1, 6) gives 1 to 5 (6 is not included).
In second loop it goes through each item in list.""",
        "points": """• Used for known number of repetitions
• range() creates sequence
• Stop value is excluded
• Can also loop over lists"""
    },
    "While Loop": {
        "concept": """while loop keeps running as long as condition is True.
Useful when we don't know exact number of repetitions.""",
        "example": """count = 1

while count <= 5:
    print(count)
    count = count + 1""",
        "explanation": """count starts from 1 and increases.
When it becomes 6 the condition becomes False and loop stops.""",
        "points": """• Checks condition before each run
• Always update the variable inside
• Forgetting update can cause infinite loop
• Use for when sequence is known"""
    },
    "Functions": {
        "concept": """Function is a block of code that does a specific task.
We write it once and can use it many times.
Created using def keyword.""",
        "example": """def add(a, b):
    result = a + b
    return result

x = add(10, 20)
print(x)""",
        "explanation": """def starts the function.
a and b are parameters. 10 and 20 are arguments.
return sends the value back.""",
        "points": """• Parameters are in definition
• Arguments are values we pass
• return is optional
• Helps avoid repeating code"""
    },
    "Lists": {
        "concept": """List stores multiple values in one variable.
It is ordered and can be changed (mutable).
Index starts from 0.""",
        "example": """numbers = [10, 20, 30]

print(numbers[0])

numbers[1] = 25
numbers.append(40)
numbers.remove(10)

print(numbers)
print(len(numbers))""",
        "explanation": """numbers[0] is first item.
append adds at end, remove deletes a value,
len() gives length.""",
        "points": """• Written with []
• Index starts at 0
• Mutable (can change)
• append() and remove() are useful
• len() gives number of items"""
    },
    "Tuples": {
        "concept": """Tuple is like list but usually cannot be changed.
Useful when values should stay fixed.
Written with parentheses.""",
        "example": """student = ("Aarjav", 18, "CSE")

print(student[0])
print(student[2])""",
        "explanation": """Index works same as list.
But we normally don't change the values after creating.""",
        "points": """• Written with ()
• Index starts at 0
• Immutable in most cases
• Use when data should not change
• Use list if you need to modify"""
    },
    "Dictionaries": {
        "concept": """Dictionary stores data as key-value pairs.
Instead of index we use keys to access values.""",
        "example": """student = {
    "name": "Aarjav",
    "age": 18,
    "course": "CSE"
}

print(student["name"])

student["age"] = 19
student["city"] = "Bhopal"

print(student)""",
        "explanation": """We access value using key like student["name"].
If key already exists it updates, otherwise adds new.""",
        "points": """• Written with {}
• Uses key-value pairs
• Keys are unique
• Can add or update easily
• keys(), values(), items() are useful methods"""
    },
    "Modules": {
        "concept": """Module is a Python file with reusable code.
We import it to use the functions inside.
Python has many built-in modules like math and random.""",
        "example": """import math
print(math.sqrt(25))

import random
print(random.randint(1, 10))""",
        "explanation": """import makes the module available.
math.sqrt calculates square root.
random.randint gives random number.""",
        "points": """• import module_name
• Helps organize code
• math for mathematical functions
• random for random values
• We can also make our own modules"""
    },
}


def wait():
    input("\nPress Enter to continue...")


def show_topic(topic_name, content):
    concept = content["concept"]
    example = content["example"]
    explanation = content["explanation"]
    points = content["points"]

    sections = [
        ("CONCEPT", concept),
        ("EXAMPLE", example),
        ("EXPLANATION", explanation),
        ("IMPORTANT POINTS", points),
    ]

    for title, text in sections:
        print("\n" + "=" * 55)
        print(topic_name.upper() + " - " + title)
        print("=" * 55)
        print(text)
        wait()


def learn_python():
    topic_names = list(TOPICS.keys())

    while True:
        print("\n" + "=" * 45)
        print("           LEARN PYTHON")
        print("=" * 45)

        for i, name in enumerate(topic_names, start=1):
            print(str(i) + ". " + name)
        print("0. Back to Main Menu")

        try:
            choice = int(input("Choose a topic: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break

        if 1 <= choice <= len(topic_names):
            selected = topic_names[choice - 1]
            show_topic(selected, TOPICS[selected])
        else:
            print("Invalid choice.")
