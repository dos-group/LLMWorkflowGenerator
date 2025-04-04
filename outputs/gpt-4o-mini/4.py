
def get_largest_city_in_germany():
    # Ask the question using the provided API
    question = "Which is the largest city in Germany?"
    answer = query_llm(question)
    
    # Print the answer
    print(answer)

# Execute the function
get_largest_city_in_germany()
