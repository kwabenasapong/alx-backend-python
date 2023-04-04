#!/usr/bin/env python3

'''
checker module for python scripts
'''


#!/usr/bin/env python3

import os
import sys
import subprocess

def check_file_header(file_path):
    """
    Check if the file starts with '#!/usr/bin/env python3'
    """
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        if first_line != '#!/usr/bin/env python3':
            print(f"Error: {file_path} doesn't start with '#!/usr/bin/env python3'")
            return False
    return True

def check_readme(file_path):
    """
    Check if a README.md file exists in the project root folder
    """
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} doesn't exist")
        return False
    if os.path.basename(file_path) != 'README.md':
        print(f"Error: {file_path} is not a README.md file")
        return False
    return True

def check_pycodestyle(file_path):
    """
    Check if the file follows pycodestyle (version 2.5) style guide
    """
    result = subprocess.run(['pycodestyle', '--version'], stdout=subprocess.PIPE)
    pycodestyle_version = result.stdout.decode('utf-8').strip()
    if pycodestyle_version != '2.10.0':
        print(f"Error: pycodestyle version 2.5.0 is required, but found {pycodestyle_version}")
        return False

    result = subprocess.run(['pycodestyle', file_path], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    if output:
        print(f"Error: {file_path} doesn't follow pycodestyle style guide")
        print(output)
        return False
    return True

def check_executable(file_path):
    """
    Check if the file is executable
    """
    if not os.access(file_path, os.X_OK):
        print(f"Error: {file_path} is not executable")
        return False
    return True

def check_file_length(file_path):
    """
    Check if the file length is within the limit
    """
    result = subprocess.run(['wc', '-l', file_path], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    file_length = int(output.split()[0])
    if file_length > 100:
        print(f"Error: {file_path} is too long ({file_length} lines, maximum is 100)")
        return False
    return True

def check_documentation(file_path):
    """
    Check if the file, classes and functions have proper documentation
    """
    try:
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        module = __import__(module_name)
    except Exception as e:
        print(f"Error: Failed to import module {module_name}: {e}")
        return False

    if not module.__doc__:
        print(f"Error: {module_name} module doesn't have documentation")
        return False

    for name, obj in module.__dict__.items():
        if isinstance(obj, type):
            if not obj.__doc__:
                print(f"Error: {module_name}.{name} class doesn't have documentation")
                return False
            for func_name, func in obj.__dict__.items():
                if callable(func):
                    if not func.__doc__:
                        print(f"Error: {module_name}.{name}.{func_name} function doesn't have documentation")
                        return False
        elif callable(obj):
            if not obj.__doc__:
                print(f"Error: {module_name}.{name} function doesn't have documentation")
                return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 checker.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not check_file_header(file_path):
        sys.exit(1)

    if not check_readme(os.path.join(os.path.dirname(file_path), 'README.md')):
        sys.exit(1)

    if not check_pycodestyle(file_path):
        sys.exit(1)

    if not check_executable(file_path):
        sys.exit(1)

    if not check_file_length(file_path):
        sys.exit(1)

    if not check_documentation(file_path):
        sys.exit(1)

    print(f"All checks passed for {file_path}")

if __name__ == '__main__':
    main()
