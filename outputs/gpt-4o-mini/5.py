
def list_files_in_current_directory():
    # Use the find_files function with an empty expression to find all files
    files = find_files("")
    return files

# Execute the function
files_in_directory = list_files_in_current_directory()
print(files_in_directory)
