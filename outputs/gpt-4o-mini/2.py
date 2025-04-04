
def get_current_temperature():
    # Get the current temperature using the provided API
    temperature = get_temperature()
    if temperature is not None:
        print(f"The current temperature is {temperature} degrees.")
    else:
        print("Could not retrieve the current temperature.")

# Execute the function
get_current_temperature()
