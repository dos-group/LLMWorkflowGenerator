
def send_car_title_to_insurance():
    # Find the contact ID for the insurance company
    contact_id = find_contact_id("insurance company")
    if contact_id is None:
        print("Could not find the contact ID for the insurance company.")
        return

    # Find the email for the insurance company using the contact ID
    email = find_contact_email(contact_id)
    if email is None:
        print("Could not find the email for the insurance company.")
        return

    # Find the car title file
    car_title_file = find_file("car title")
    if car_title_file is None:
        print("Could not find the car title file.")
        return

    # Send the car title to the insurance company
    subject = "Car Title Document"
    text = "Please find attached the car title document."
    send_email(email, subject, text, [car_title_file])
    print("Car title sent to the insurance company.")

# Call the function
send_car_title_to_insurance()
