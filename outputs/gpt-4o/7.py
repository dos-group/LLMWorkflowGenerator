
def summarize_wikipedia_article():
    # Define the URL of the Wikipedia article
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    
    # Fetch the content of the Wikipedia article
    headers = {}
    article_content = http_get_request(url, headers)
    
    # Generate a summary of the article using the LLM
    summary = query_llm(f"Summarize the following article: {article_content}")
    
    # Print the summary
    print(summary)

# Execute the function
summarize_wikipedia_article()
