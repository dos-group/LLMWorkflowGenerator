
def list_all_files_in_current_directory():
    # Use the find_files function with a wildcard expression to find all files
    files = find_files("*")
    # Print each file name
    for file in files:
        print(file)

# Call the function
list_all_files_in_current_directory()
