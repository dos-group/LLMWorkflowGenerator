
def install_nginx_on_machine():
    ssh_command = "ssh -o StrictHostKeyChecking=no root@127.0.0.1 -p 2222 'apt-get update && apt-get install -y nginx'"
    shell(ssh_command)

install_nginx_on_machine()
