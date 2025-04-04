
def execute_instruction(instruction: str):
    contact_id = find_contact_id(instruction)
    if contact_id is None:
        print("Contact ID not found.")
        return

    contact_email = find_contact_email(contact_id)
    if contact_email is None:
        print("Contact email not found.")
        return

    question = f"Do you want to install nginx on your machine? (Yes/No)"
    response = ask_question(question)
    if response.lower() != "yes":
        print("Installation cancelled.")
        return

    subject = "Nginx Installation Request"
    text = "Please install nginx on your machine."
    attachment_paths = find_files("nginx_install_script.sh")
    if not attachment_paths:
        print("No installation script found.")
        return

    send_email(contact_email, subject, text, attachment_paths)
    print("Email sent with installation script.")

execute_instruction("Please install nginx on the machine with the address 127.0.0.1:2222 running Debian GNU/Linux")
