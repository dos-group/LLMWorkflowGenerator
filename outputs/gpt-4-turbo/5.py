
def list_all_files_in_current_directory():
    # Using the find_files function with a wildcard to match all files in the current directory
    all_files = find_files("*")
    return all_files

# Call the function and print the result
files_in_directory = list_all_files_in_current_directory()
print("Files in the current directory:", files_in_directory)
