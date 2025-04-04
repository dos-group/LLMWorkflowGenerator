
def respond_to_instruction():
    random_number = generate_random_number(1, 101)
    return_message = f"Here is a random number between 1 and 100: {random_number}"
    print(return_message)

respond_to_instruction()
