
def summarize_wikipedia_article():
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    headers = {}
    response = http_get_request(url, headers)
    summary_query = "Please summarize this text: " + response
    summary = query_llm(summary_query)
    print(summary)

# Execute the function
summarize_wikipedia_article()
