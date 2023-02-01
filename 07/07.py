from collections import defaultdict

def move_up(current_directory): # "delete" last directory name from string current_directory
    return "/".join(current_directory.split("/")[:-1])

def add_file(path, size):
    #add file size to current dir and move up to add it all parent dirs all the way to root
    while True:
        directories[path] += size
        if path.split("/")[-1] == "root":
            break
        path = move_up(path)

def count_dir_sizes(lines):
    current_directory = ""
    for line in lines: #ignore all lines except "$ cd" and "files"
        if line.startswith("$ cd"):
            if ".." in line:
                current_directory = move_up(current_directory)
            else:
                current_directory += "/" + line.split(" ")[2]
        elif line.split(" ")[0].isnumeric():
            add_file(current_directory, int(line.split(" ")[0]))

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

directories = defaultdict(lambda: 0) #key: value - complete path: size
count_dir_sizes(lines)

#Part 1: sum of all directories larger than 100.000
large_directories = [directory for directory in directories.values() if directory < 100000]
print("Task 1:", sum(large_directories))

#Part 2: size of smallest directory, that might be deleted, that free space at least 30.000.000
size_to_be_cleared = 30000000 - (70000000 - directories["/root"])
large_directories = [directory for directory in directories.values() if directory >= size_to_be_cleared]
print("Task 2:",min(large_directories))