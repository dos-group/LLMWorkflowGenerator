
def send_car_title_to_insurance():
    # Step 1: Find the car title file
    car_title_files = find_files("car title")
    if not car_title_files:
        print("No car title file found.")
        return
    
    car_title_file = car_title_files[0]  # Assuming we take the first found file

    # Step 2: Find the insurance company's contact ID and email
    insurance_contact_id = find_contact_id("insurance company")
    if insurance_contact_id is None:
        print("Insurance company not found.")
        return
    
    insurance_email = find_contact_email(insurance_contact_id)
    if insurance_email is None:
        print("Insurance company email not found.")
        return

    # Step 3: Send the email with the car title attached
    subject = "Car Title Submission"
    text = "Please find attached my car title."
    attachment_paths = [car_title_file]
    
    send_email(insurance_email, subject, text, attachment_paths)
    print("Car title sent to insurance company.")

# Execute the function
send_car_title_to_insurance()
