
def summarize_wiki_article(url: str) -> str:
    response = http_get_request(url, {})
    query = f"Please summarize the following article:\n{response}"
    summary = query_llm(query)
    return summary

# Call the function and print the result
print(summarize_wiki_article("https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"))
