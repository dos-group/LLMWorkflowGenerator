
def get_current_directory_files():
    expression = ".*"  # Regular expression to match all files
    files = find_files(expression)
    for file in files:
        print(file)

get_current_directory_files()
