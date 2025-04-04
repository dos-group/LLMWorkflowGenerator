WITH FIXED MARKER

def process_request():
    contact_id = find_contact_id("insurance company")
    if contact_id is None:
        print("Contact not found.")
        return

    email = find_contact_email(contact_id)
    if email is None:
        print("Email not found for the contact.")
        return

    question = ask_question(f"Do you want to send the car title to {email}? (yes/no)")
    if question.lower() != "yes":
        print("Email not sent.")
        return

    temperature = get_temperature()
    print(f"Current temperature: {temperature}")

    files = find_files("car_title*")
    if not files:
        print("No car title files found.")
        return

    attachment_paths = [file for file in files]
    send_email(email, "Car Title", "Here is your car title.", attachment_paths)
    print("Email sent successfully.")

process_request()
