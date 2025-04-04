
def list_files_in_current_directory():
    # Use the find_files function to get all files in the current directory
    files = find_files(".")
    return files

# Execute the function and print the result
files_in_directory = list_files_in_current_directory()
print(files_in_directory)
