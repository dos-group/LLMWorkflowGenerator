
def send_car_title_to_insurance():
    # Step 1: Find the contact ID for the insurance company
    insurance_contact_id = find_contact_id("insurance company")
    if insurance_contact_id is None:
        print("Insurance company contact not found.")
        return

    # Step 2: Get the email address of the insurance company
    insurance_email = find_contact_email(insurance_contact_id)
    if insurance_email is None:
        print("Email address for insurance company not found.")
        return

    # Step 3: Find the car title file
    car_title_file = find_file("car title")
    if car_title_file is None:
        print("Car title file not found.")
        return

    # Step 4: Send the email with the car title attached
    send_email(
        email=insurance_email,
        subject="Car Title Document",
        text="Attached is the car title document for processing.",
        attachment_paths=[car_title_file]
    )
    print("Car title sent to insurance company.")

# Call the function
send_car_title_to_insurance()
