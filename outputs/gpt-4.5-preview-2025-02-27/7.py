
def summarize_wikipedia_article():
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    headers = {"Accept": "text/html"}
    html_content = http_get_request(url, headers)
    
    # Prepare a query for the LLM to summarize the article
    query = f"Summarize the following Wikipedia article content:\n\n{html_content}"
    
    # Get the summary from the LLM
    summary = query_llm(query)
    
    # Print the summary
    print(summary)

# Execute the function
summarize_wikipedia_article()
