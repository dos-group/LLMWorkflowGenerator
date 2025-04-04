
def summarize_wikipedia_article():
    # Fetch the content of the Wikipedia article
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    headers = {}
    article_content = http_get_request(url, headers)
    
    # Query the language model to summarize the article
    summary = query_llm(f"Please summarize the following text: {article_content}")
    
    # Print the summary
    print(summary)

# Call the function to execute the task
summarize_wikipedia_article()
