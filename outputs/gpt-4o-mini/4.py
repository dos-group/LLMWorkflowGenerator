
def get_largest_city_in_germany():
    # Ask the question using the provided API
    question = "Which is the largest city in Germany?"
    answer = query_llm(question)
    return answer

# Execute the function
largest_city = get_largest_city_in_germany()
print(largest_city)
