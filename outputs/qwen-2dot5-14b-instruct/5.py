
def list_files_in_directory():
    # Use the find_files function to get all files in the current directory
    files = find_files("*")
    # Print each file found
    for file in files:
        print(file)
