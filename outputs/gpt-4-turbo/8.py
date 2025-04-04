
def install_nginx_on_remote_machine():
    # Command to install nginx on a Debian-based system
    install_command = "sudo apt-get update && sudo apt-get install -y nginx"
    
    # SSH command to connect to the remote machine and execute the installation command
    ssh_command = f"ssh -p 2222 root@127.0.0.1 '{install_command}'"
    
    # Execute the command using the shell function from the API
    result = shell(ssh_command)
    
    # Print the output of the shell command
    print(result)
