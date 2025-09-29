
def respond_to_temperature_query():
    temperature = get_temperature()
    response = f"The current temperature is {temperature} degrees."
    print(response)

respond_to_temperature_query()
