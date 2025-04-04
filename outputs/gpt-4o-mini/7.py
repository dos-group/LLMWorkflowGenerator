
def summarize_transformer_article():
    # Step 1: Fetch the content of the Wikipedia article
    url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
    headers = {"User-Agent": "Mozilla/5.0"}
    article_content = http_get_request(url, headers)
    
    # Step 2: Ask the LLM to summarize the article content
    summary = query_llm(article_content)
    
    # Step 3: Print the summary
    print(summary)

# Execute the function
summarize_transformer_article()
