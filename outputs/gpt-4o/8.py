
def install_nginx_on_remote_machine():
    # Use the shell function to install nginx on the remote machine
    command = "ssh -p 2222 user@127.0.0.1 'sudo apt-get update && sudo apt-get install -y nginx'"
    shell(command)

# Call the function
install_nginx_on_remote_machine()
