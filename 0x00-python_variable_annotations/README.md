# 0x00. Python - Variable Annotations

## Resources

**Read or watch**:

-   [PEP 484 -- Type Hints](https://intranet.hbtn.io/rltoken/8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z "PEP 484 -- Type Hints")
-   [PEP 526 -- Syntax for Variable Annotations](https://intranet.hbtn.io/rltoken/8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z "PEP 526 -- Syntax for Variable Annotations")
-   [Type Checking](https://intranet.hbtn.io/rltoken/8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z "Type Checking")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z "explain to anyone"),  **without the help of Google**:

### General

-   What are type annotations, and how to use them
-   What are the  `typing`  module's types and how to use them
-   How to validate your code with  `mypy`

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  `python3`  (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/env python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `pycodestyle`  style (version 2.5)
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   All your functions and coroutines must be type-annotated.
-   All your variables should be annotated as well

### Python Unit Tests

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   You have to use the  `unittest`  module
-   All your test files should be python files (extension:  `.py`)
-   All your test files and folders should start by  `test_`
-   Your file organization in the tests folder should be the same as your project: ex: for  `models/base_model.py`, unit tests must be in:  `tests/test_models/test_base_model.py`
-   All your tests should be executed by using this command:  `python3 -m unittest discover tests`
-   You can also test file by file by using this command:  `python3 -m unittest tests/test_models/test_base_model.py`
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## More Info

### Install  `mypy`

```
$ pip3 install mypy

```

### Install  `pycodestyle`

```
$ pip3 install pycodestyle

```

### Tests

We strongly encourage you to work together on test cases, so that you don’t miss any edge case.  [Here](https://intranet.hbtn.io/rltoken/8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z "Here")  is a  [Google Doc](https://intranet.hbtn.io/rltoken/8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z8Z "Google Doc")  to collaborate on test cases. If the link is unavailable ask for it in the  `#correction-0x00-python-variable_annotations`  Slack channel.

## Tasks

### 0. Basic annotations - add

mandatory

Write a type-annotated function  `def add(a: float, b: float) -> float:`  that returns the sum of two floats.

-   `a`  and  `b`  are floats
-   Returns their sum as a float.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

add = __import__('0-add').add

print(add(1, 2))
print(add(1.5, 2.5))
print(add("Holberton", 89))

bob@dylan:~$ ./0-main.py
3.0
4.0
Holberton89
bob@dylan:~$ mypy 0-main.py
Success: no issues found in 1 source file
bob@dylan:~$ cat 0-add.py
#!/usr/bin/env python3
""" Basic annotations - add """
from typing import Union


def add(a: float, b: float) -> float:
    """ Returns the sum of two floats """
    return a + b
bob@dylan:~$ mypy 0-add.py
Success: no issues found in 1 source file

```

Repo:

GitHub repository: alx-backend-python
Directory: 0x00-python_variable_annotations
File: 0-add.py
  
  Done?  Help  Get a sandbox

### 1. Basic annotations - concat

mandatory

Write a type-annotated function  `def concat(str1: str, str2: str) -> str:`  that returns a concatenated string.

-   `str1`  and  `str2`  are strings
-   Returns their concatenation

```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

concat = __import__('1-concat').concat

print(concat("Hello", " Holberton"))
print(concat("1", "2"))

bob@dylan:~$ ./1-main.py
Hello Holberton
12
bob@dylan:~$ mypy 1-main.py
Success: no issues found in 1 source file
bob@dylan:~$ cat 1-concat.py
#!/usr/bin/env python3
""" Basic annotations - concat """
from typing import Union


def concat(str1: str, str2: str) -> str:
    """ Returns a concatenated string """
    return str1 + str2
bob@dylan:~$ mypy 1-concat.py
Success: no issues found in 1 source file

```

Repo:

GitHub repository: alx-backend-python
Directory: 0x00-python_variable_annotations
File: 1-concat.py
  
  Done?  Help  Get a sandbox

### 2. Basic annotations - floor

mandatory

Write a type-annotated function  `def floor(n: float) -> int:`  that returns the floor of the float.

-   `n`  is a float
-   Returns the floor of the float

```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

floor = __import__('2-floor').floor


print(floor(2.5))
print(floor(2.4))

bob@dylan:~$ ./2-main.py
2
2
bob@dylan:~$ mypy 2-main.py
Success: no issues found in 1 source file
bob@dylan:~$ cat 2-floor.py
#!/usr/bin/env python3
""" Basic annotations - floor """
from typing import Union


def floor(n: float) -> int:
    """ Returns the floor of the float """
    return int(n)
bob@dylan:~$ mypy 2-floor.py
Success: no issues found in 1 source file

```

Repo:

GitHub repository: alx-backend-python
Directory: 0x00-python_variable_annotations
File: 2-floor.py
  
  Done?  Help  Get a sandbox

### 3. Basic annotations - to string
