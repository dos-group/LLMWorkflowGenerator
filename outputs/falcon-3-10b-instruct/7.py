
def summarize_wikipedia_article(url: str) -> str:
    query = f"Summarize the Wikipedia article at {url}"
    summary = query_llm(query)
    return summary

# Call the function with the provided URL
wikipedia_url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"
summary = summarize_wikipedia_article(wikipedia_url)
print(summary)
