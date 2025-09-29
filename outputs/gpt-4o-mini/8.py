
def install_nginx():
    # Define the command to install nginx on Debian
    command = "ssh -p 2222 user@127.0.0.1 'sudo apt update && sudo apt install -y nginx'"
    
    # Execute the command
    result = shell(command)
    
    # Print the result of the command execution
    print(result)

# Execute the function to install nginx
install_nginx()
