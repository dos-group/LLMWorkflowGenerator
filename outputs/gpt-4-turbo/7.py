
def summarize_wikipedia_article():
    # URL of the Wikipedia article
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    
    # Headers for the HTTP GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    # Perform HTTP GET request to fetch the article
    article_html = http_get_request(url, headers)
    
    # Query the language model to summarize the article
    summary = query_llm(f"Please summarize the following content: {article_html}")
    
    # Print the summary
    print(summary)

# Call the function to summarize the Wikipedia article
summarize_wikipedia_article()
