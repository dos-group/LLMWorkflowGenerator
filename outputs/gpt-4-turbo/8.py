
def install_nginx_on_debian():
    # Command to install nginx on a Debian machine
    install_command = "ssh -p 2222 root@127.0.0.1 'apt-get update && apt-get install -y nginx'"
    
    # Execute the shell command using the shell function from the API
    result = shell(install_command)
    
    # Print the result of the installation command
    print(f"Installation result: {result}")

# Call the function to install nginx
install_nginx_on_debian()
