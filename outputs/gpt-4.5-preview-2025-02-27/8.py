
def install_nginx_on_remote_machine():
    command = "ssh -p 2222 127.0.0.1 'sudo apt-get update && sudo apt-get install -y nginx'"
    result = shell(command)
    print(result)

install_nginx_on_remote_machine()
