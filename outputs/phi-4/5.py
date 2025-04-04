
def list_files_in_current_directory():
    # Use the find_files function with an expression that matches all files in the current directory
    files = find_files(".")

    # Print the list of files
    if files is not None:
        for file in files:
            print(file)
    else:
        print("No files found or an error occurred.")

# Call the function
list_files_in_current_directory()
