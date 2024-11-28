def list_files_in_home_directory():
    # Use a shell command to list files in the home directory
    home_directory_files = shell("ls ~")
    play_voice("The files in your home directory are as follows: " + home_directory_files)

list_files_in_home_directory()
