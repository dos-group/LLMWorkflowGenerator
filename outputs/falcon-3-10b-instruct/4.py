
def answer_question(question: str) -> str:
    # Step 1: Query the Large Language Model (LLM) to get the answer
    llm_response = query_llm(question)

    # Step 2: Find the contact ID for the email service
    contact_id = find_contact_id("email_service")

    # Step 3: Find the email address associated with the contact ID
    email = find_contact_email(contact_id)

    # Step 4: Ask the user if they want to receive the answer via email
    receive_email = ask_question("Do you want to receive the answer via email? (yes/no)")

    # Step 5: If the user wants to receive the answer via email, send it
    if receive_email.lower() == "yes":
        send_email(email, "Answer to your question", llm_response, [])

    # Step 6: Print the answer to the console
    print(llm_response)

# Call the function with the given question
answer_question("Which is the largest city in Germany?")
