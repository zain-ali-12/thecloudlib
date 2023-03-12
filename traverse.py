import os
import time

root = os.getcwd()
exclude_list = ["cloudlib-venv"]
filenames = []


def traverse(directory):
    os.chdir(directory)
    folders = [os.path.abspath(folder) for folder in os.listdir(os.getcwd()) if os.path.isdir(folder) and folder[0] not in [".", "_"] and folder not in exclude_list]
    [filenames.append(os.path.abspath(file)) for file in os.listdir(os.getcwd()) if os.path.isfile(file) and file.split(".")[-1] in ["py", "txt", "csv", "html", "css", "js"]]
    [traverse(path) for path in folders]
    return filenames


traverse(os.getcwd())

total_lines = 0
for path in filenames:

    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
            print(f"{path} has {lines} lines of code")
            total_lines += lines
    except UnicodeDecodeError:
        with open(path, 'rb') as f:
            lines = len(f.readlines())
            print(f"{path} has {lines} lines of code")
            total_lines += lines

print(f"In total, this project has {total_lines} of code!")
