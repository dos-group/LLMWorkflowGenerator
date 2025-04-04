
def install_nginx_on_remote_machine():
    # Use SSH to connect to the remote machine and install nginx
    command = (
        "ssh -p 2222 user@127.0.0.1 "
        "'sudo apt-get update && sudo apt-get install -y nginx'"
    )
    result = shell(command)
    print(result)

# Execute the function
install_nginx_on_remote_machine()
