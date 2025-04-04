
def summarize_wikipedia_article():
    # Define the URL of the Wikipedia article
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    
    # Perform an HTTP GET request to fetch the article content
    headers = {}
    article_content = http_get_request(url, headers)
    
    # Use the query_llm function to summarize the article content
    summary = query_llm(f"Summarize the following article content: {article_content}")
    
    # Print the summary
    print(summary)

# Call the function to summarize the Wikipedia article
summarize_wikipedia_article()
