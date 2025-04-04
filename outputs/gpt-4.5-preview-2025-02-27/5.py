
def list_all_files_in_current_directory():
    files = find_files("*")
    if files:
        print("Files in the current directory:")
        for file in files:
            print(file)
    else:
        print("No files found in the current directory.")

# Execute the function
list_all_files_in_current_directory()
