
def find_largest_city_in_germany():
    # Use the query_llm function to get information about the largest city in Germany
    response = query_llm("Which is the largest city in Germany?")
    
    # Extract the city name from the response
    # Assuming the response is a simple string with the city name
    city_name = response.strip()
    
    # Print the result
    print(f"The largest city in Germany is: {city_name}")

# Call the function
find_largest_city_in_germany()
