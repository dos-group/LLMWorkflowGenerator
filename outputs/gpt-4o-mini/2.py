
def get_current_temperature():
    # Get the current temperature using the provided API
    temperature = get_temperature()
    return temperature

# Execute the function to get the current temperature
current_temperature = get_current_temperature()
print(f"The current temperature is: {current_temperature}°C")
