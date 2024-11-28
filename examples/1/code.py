# Step 1: Find the car title file ID
car_title_id = find_file_id("car title")
if car_title_id is None:
    print_screen("Car title file not found.")
else:
    # Step 2: Find the insurance company contact ID
    insurance_contact_id = find_contact_id("insurance company")
    if insurance_contact_id is None:
        print_screen("Insurance company contact not found.")
    else:
        # Step 3: Get the insurance company's email address
        insurance_email = find_contact_email(insurance_contact_id)
        if insurance_email is None:
            print_screen("Insurance company email not found.")
        else:
            # Step 4: Prepare the email subject and body
            subject = "Car Title Submission"
            text = "Please find attached my car title."
            attachments = [car_title_id]

            # Step 5: Send the email with the car title attached
            send_email(insurance_email, subject, text, attachments)

            # Confirmation message
            print_screen("Car title sent to insurance company.")
