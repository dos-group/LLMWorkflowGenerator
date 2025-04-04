
def get_random_number():
    # Generate a random number between 1 and 100
    random_number = generate_random_number(1, 101)  # 101 is exclusive
    return random_number

# Execute the function
random_number = get_random_number()
print(random_number)
