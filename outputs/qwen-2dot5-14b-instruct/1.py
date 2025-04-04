
def random_number_response():
    random_number = generate_random_number(1, 101)
    return ask_question(f"The random number between 1 and 100 is: {random_number}")

print(random_number_response())
