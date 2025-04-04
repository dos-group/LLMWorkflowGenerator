
def send_car_title_to_insurance():
    # Find the contact ID for the insurance company
    insurance_contact_id = find_contact_id("insurance company")
    if insurance_contact_id is None:
        print("Insurance company contact not found.")
        return
    
    # Get the email address of the insurance company
    insurance_email = find_contact_email(insurance_contact_id)
    if insurance_email is None:
        print("Insurance company email not found.")
        return
    
    # Find the car title file
    car_title_file = find_file("car title")
    if car_title_file is None:
        print("Car title file not found.")
        return
    
    # Send the email with the car title attached
    subject = "Car Title Document"
    text = "Please find attached my car title."
    send_email(insurance_email, subject, text, [car_title_file])
    print("Car title sent successfully.")

# Call the function
send_car_title_to_insurance()
