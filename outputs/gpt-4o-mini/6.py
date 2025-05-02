
def send_car_title_to_insurance():
    # Step 1: Find the car title file
    car_title_file = find_file("car title")
    
    if car_title_file is None:
        print("Car title file not found.")
        return
    
    # Step 2: Find the contact ID for the insurance company
    insurance_contact_id = find_contact_id("insurance company")
    
    if insurance_contact_id is None:
        print("Insurance company contact not found.")
        return
    
    # Step 3: Retrieve the email address of the insurance company
    insurance_email = find_contact_email(insurance_contact_id)
    
    if insurance_email is None:
        print("Insurance company email not found.")
        return
    
    # Step 4: Send the email with the car title attached
    subject = "Car Title Submission"
    text = "Please find attached my car title."
    attachment_paths = [car_title_file]
    
    send_email(insurance_email, subject, text, attachment_paths)

# Execute the function
send_car_title_to_insurance()
