
def list_all_files_in_directory():
    # Using the API function to find all files with a wildcard expression that matches all files
    all_files = find_files("*")
    
    # Printing each file found
    for file in all_files:
        print(file)

# Execute the function
list_all_files_in_directory()
