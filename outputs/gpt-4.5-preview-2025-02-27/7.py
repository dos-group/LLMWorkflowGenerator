
def summarize_wikipedia_article(url: str):
    headers = {"Accept": "text/html"}
    article_html = http_get_request(url, headers)
    
    query = f"Summarize the following Wikipedia article content:\n\n{article_html}"
    summary = query_llm(query)
    
    print(summary)

# Call the function with the provided URL
summarize_wikipedia_article("https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)")
