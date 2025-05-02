
def list_files():
    files = find_files("")
    print("Files in the current directory:")
    for file in files:
        print(file)

list_files()
