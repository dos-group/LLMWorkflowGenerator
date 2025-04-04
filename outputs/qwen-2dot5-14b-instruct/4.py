
def get_largest_city_in_germany():
    query = "Which is the largest city in Germany?"
    answer = query_llm(query)
    print(f"The largest city in Germany is: {answer}")

# Execute the function
get_largest_city_in_germany()
