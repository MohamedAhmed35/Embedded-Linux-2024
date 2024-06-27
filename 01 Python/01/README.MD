# Embedded Linux Diploma

## Create Your First "Hello, World!" Program

### Steps to Create "Hello, World!"

#### 1. Create python file from terminal
>      touch hello.py
#### 2. Write the following code in file:
>      print("Hello, World!")
#### 3. Run the script from the terminal
>      python3 hello.py

### Variables
#### Unlike other programming language, python has no command for declaring a vairable.
#### A variable is created the moment you first assign a value to it.
>      x = 5
>      print(type(x)
>      x = "ahmed"
>      print(type(x))
>      x = 3.5
>      print(type(x))
##### comma Operator
>      x, y , z = 1, 2.5, 'M'
>      print(x)
>      print(y)
>      print(z)

### Python Data Types
#### 1. Integer (int): Integer represent the whole number without any decimal point. They can be positive or negative.
#### Example:
>        x = 5
>        x = -5
#### 2. Float (float): Float represent real numbers with a decimal point. They can also be positive or negative.
>        height = 179.3
>        temperature = -18.7
#### 3. String (str): Strings are sequence of characters, enclosed within single qoutes (') or double quotes (").
>        name = John
>        message = "Hello, World!"
#### 4. Boolean( bool): Booleans represent truth values. (True or False)
>        is_right = True
#### 5. List (list): Lists are ordered collection of items, which can be different types. They are mutuable, meaning          thier element can be changed after creation.
>        items = ['M', 2.5, '4', 'Weather']
#### 6. Tuple (tuple): Tuples are similar to lists, they are ordered collection of items of different type, but are           immutable, meanning their elements cannot be changed after creating.
>        colors = ('red', 'green', 'blue')
>        items = ('M', 2.5, '4', 'Weather')
#### 7. Dictionary (dict): Dictionaries are unordered collections of key-value pairs. They are mutable and indexed by         keys. In case of duplicate pair, it override the previous pair.
>        dic = {'brand': 'Ford", "electric": Flase, "Year": 1964, "colors": ["red", "white", "blue"]}
#### 8. Set (set): Sets are unordered collection of unique elements. They are mutuable but do not allow duplicate             items
>        unique_numbers = {1, 2, 3, 4, 5}
>        unique_words = {"apple", "banana", "cherry"}
