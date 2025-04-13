# Python Quiz Questions
quiz_data = [
    {
        "question": "What is a dynamically typed language?",
        "a": "A language where types are checked at compile-time",
        "b": "A language where types are checked at runtime",
        "c": "A language that does not support typing",
        "d": "A language with fixed data types",
        "correct": "b",
        "explanation": "In dynamically typed languages like Python, the type is checked during runtime, allowing for more flexibility."
    },
    {
        "question": "What is the purpose of the 'self' parameter in Python class methods?",
        "a": "It's a keyword for defining class methods",
        "b": "It refers to the instance of the class",
        "c": "It's used to create static methods",
        "d": "It's a placeholder and has no specific purpose",
        "correct": "b",
        "explanation": "In Python, 'self' refers to the instance of the class and is used to access instance variables and methods."
    },
    {
        "question": "What does the 'yield' keyword do in Python?",
        "a": "Terminates a function",
        "b": "Creates a generator function",
        "c": "Imports a module",
        "d": "Defines a class",
        "correct": "b",
        "explanation": "The 'yield' keyword is used to create a generator function, which returns an iterator."
    },
    {
        "question": "What is a lambda function in Python?",
        "a": "A named function defined using the 'def' keyword",
        "b": "An anonymous function defined using the 'lambda' keyword",
        "c": "A built-in function in Python's standard library",
        "d": "A function that always returns True or False",
        "correct": "b",
        "explanation": "A lambda function is an anonymous function in Python, defined using the 'lambda' keyword."
    },
    {
        "question": "What is the purpose of the '__init__' method in Python classes?",
        "a": "To initialize class variables",
        "b": "To define class methods",
        "c": "To create a new instance of the class",
        "d": "To delete an instance of the class",
        "correct": "a",
        "explanation": "The '__init__' method is used to initialize class variables when a new instance of the class is created."
    },
    {
        "question": "What does the 'with' statement do in Python?",
        "a": "Defines a new function",
        "b": "Creates a loop",
        "c": "Handles resource management and cleanup",
        "d": "Imports a module",
        "correct": "c",
        "explanation": "The 'with' statement in Python is used for resource management, ensuring proper acquisition and release of resources."
    },
    {
        "question": "What is a decorator in Python?",
        "a": "A function that takes another function as an argument",
        "b": "A class method",
        "c": "A type of loop",
        "d": "A built-in data structure",
        "correct": "a",
        "explanation": "A decorator in Python is a function that takes another function as an argument and extends its behavior without modifying it."
    },
    {
        "question": "What is the purpose of the 'pass' statement in Python?",
        "a": "To skip the rest of the loop",
        "b": "To raise an exception",
        "c": "To do nothing and act as a placeholder",
        "d": "To return a value from a function",
        "correct": "c",
        "explanation": "The 'pass' statement in Python is used as a placeholder for future code, allowing empty code blocks that do nothing."
    },
    {
        "question": "What is the difference between '==' and 'is' in Python?",
        "a": "'==' compares values, 'is' compares memory addresses",
        "b": "'==' is for numbers, 'is' is for strings",
        "c": "They are interchangeable",
        "d": "'==' is a keyword, 'is' is an operator",
        "correct": "a",
        "explanation": "'==' compares the values of objects, while 'is' compares their memory addresses (identity)."
    },
    {
        "question": "What is a list comprehension in Python?",
        "a": "A way to create lists using a for loop",
        "b": "A built-in function to manipulate lists",
        "c": "A concise way to create lists based on existing lists",
        "d": "A method to sort lists",
        "correct": "c",
        "explanation": "List comprehension is a concise way to create new lists based on existing lists or other iterable objects in Python."
    },
    # Additional beginner-friendly questions
    {
        "question": "Which of the following is NOT a Python data type?",
        "a": "List",
        "b": "Dictionary",
        "c": "Array",
        "d": "Tuple",
        "correct": "c",
        "explanation": "Array is not a built-in data type in Python. Python uses Lists instead, though NumPy provides array functionality."
    },
    {
        "question": "How do you create a comment in Python?",
        "a": "// This is a comment",
        "b": "/* This is a comment */",
        "c": "# This is a comment",
        "d": "-- This is a comment",
        "correct": "c",
        "explanation": "In Python, comments start with the # symbol and extend to the end of the line."
    },
    {
        "question": "What will print(2 ** 3) output in Python?",
        "a": "6",
        "b": "8",
        "c": "5",
        "d": "Error",
        "correct": "b",
        "explanation": "The ** operator in Python represents exponentiation. 2 ** 3 means 2 raised to the power of 3, which equals 8."
    },
    {
        "question": "How do you define a function in Python?",
        "a": "function myFunc():",
        "b": "def myFunc():",
        "c": "create myFunc():",
        "d": "func myFunc():",
        "correct": "b",
        "explanation": "In Python, functions are defined using the 'def' keyword followed by the function name and parentheses."
    },
    {
        "question": "What does the len() function do in Python?",
        "a": "Returns the largest item in an iterable",
        "b": "Returns the smallest item in an iterable",
        "c": "Returns the length of an object",
        "d": "Returns the average of all items in an iterable",
        "correct": "c",
        "explanation": "The len() function returns the number of items in an object like a string, list, or dictionary."
    },
    {
        "question": "How do you add an element to the end of a list in Python?",
        "a": "list.add(element)",
        "b": "list.append(element)",
        "c": "list.insert(element)",
        "d": "list.push(element)",
        "correct": "b",
        "explanation": "The append() method adds an element to the end of a list in Python."
    },
    {
        "question": "What is the correct way to create an empty list in Python?",
        "a": "list = []",
        "b": "list = {}",
        "c": "list = ()",
        "d": "list = ''",
        "correct": "a",
        "explanation": "An empty list in Python is created using square brackets []."
    },
    {
        "question": "What does the 'print()' function do in Python?",
        "a": "Prints a document",
        "b": "Displays output to the console",
        "c": "Creates a new line",
        "d": "Imports a module",
        "correct": "b",
        "explanation": "The print() function in Python displays the specified message or value to the standard output (usually the console)."
    },
    {
        "question": "Which of these is NOT a valid variable name in Python?",
        "a": "my_var",
        "b": "_myVar",
        "c": "1var",
        "d": "myVar",
        "correct": "c",
        "explanation": "Variable names in Python cannot start with a number. They must start with a letter or underscore."
    },
    {
        "question": "What is the output of print('Hello' + 'World')?",
        "a": "Hello World",
        "b": "HelloWorld",
        "c": "Hello+World",
        "d": "Error",
        "correct": "b",
        "explanation": "The + operator concatenates strings in Python without adding spaces. So 'Hello' + 'World' becomes 'HelloWorld'."
    },
    {
        "question": "How do you convert a string to an integer in Python?",
        "a": "to_int(string)",
        "b": "int(string)",
        "c": "string.toInteger()",
        "d": "convert(string, int)",
        "correct": "b",
        "explanation": "The int() function converts a string to an integer in Python."
    },
    {
        "question": "What is the correct way to check if two variables are equal in Python?",
        "a": "if x = y:",
        "b": "if x == y:",
        "c": "if x === y:",
        "d": "if x equals y:",
        "correct": "b",
        "explanation": "In Python, the equality operator is ==. The single = is used for assignment, not comparison."
    },
    {
        "question": "What does the following code output? print(bool(0))",
        "a": "0",
        "b": "1",
        "c": "True",
        "d": "False",
        "correct": "d",
        "explanation": "In Python, 0 is considered False when converted to a boolean. All other numbers convert to True."
    },
    {
        "question": "Which method is used to remove whitespace from the beginning and end of a string?",
        "a": "strip()",
        "b": "trim()",
        "c": "remove()",
        "d": "clean()",
        "correct": "a",
        "explanation": "The strip() method removes whitespace from the beginning and end of a string in Python."
    },
    {
        "question": "What is the correct way to import a module in Python?",
        "a": "import module",
        "b": "include module",
        "c": "using module",
        "d": "require module",
        "correct": "a",
        "explanation": "In Python, modules are imported using the 'import' keyword followed by the module name."
    },
    {
        "question": "What is the output of print(3 > 2 and 1 > 2)?",
        "a": "True",
        "b": "False",
        "c": "None",
        "d": "Error",
        "correct": "b",
        "explanation": "The 'and' operator returns True if both conditions are True. Here, 3 > 2 is True but 1 > 2 is False, so the result is False."
    },
    {
        "question": "How do you create a dictionary in Python?",
        "a": "dict = ()",
        "b": "dict = []",
        "c": "dict = {}",
        "d": "dict = <>",
        "correct": "c",
        "explanation": "Dictionaries in Python are created using curly braces {}."
    },
    {
        "question": "What is the output of print(type([]))?",
        "a": "<class 'list'>",
        "b": "<class 'array'>",
        "c": "<class 'tuple'>",
        "d": "<class 'dict'>",
        "correct": "a",
        "explanation": "The type() function returns the type of an object. [] creates an empty list, so the output is <class 'list'>."
    },
    {
        "question": "What is the correct way to create a for loop in Python?",
        "a": "for i = 0; i < 5; i++:",
        "b": "for i in range(5):",
        "c": "for (i = 0; i < 5; i++):",
        "d": "for each i in range(5):",
        "correct": "b",
        "explanation": "In Python, for loops are typically used with the 'in' keyword to iterate over a sequence like range(5)."
    },
    {
        "question": "What is the purpose of the 'if __name__ == \"__main__\":' statement?",
        "a": "To check if the file is the main program being run",
        "b": "To define the main function",
        "c": "To import the main module",
        "d": "To check if the program has any errors",
        "correct": "a",
        "explanation": "This statement checks if the script is being run directly (as the main program) or being imported as a module into another script."
    }
]
