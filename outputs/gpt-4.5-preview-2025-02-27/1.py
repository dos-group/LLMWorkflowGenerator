
def tell_random_number():
    number = generate_random_number(1, 101)  # exclusiveEnd is 101 to include 100
    print(f"Your random number is: {number}")

# Call the function
tell_random_number()
