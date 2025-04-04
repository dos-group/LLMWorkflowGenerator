
def install_nginx():
    # Simulate SSH login and execute commands to install nginx
    ssh_command = "ssh root@127.0.0.1 -p 2222 'apt-get update && apt-get install -y nginx'"
    shell(ssh_command)

# Execute the function
install_nginx()
