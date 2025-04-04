
def summarize_wikipedia_article(url):
    # Query the language model with the URL to get a summary
    summary = query_llm(f"Summarize the content of the following URL: {url}")
    return summary

# URL of the Wikipedia article
url = "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"

# Summarize the article
summary = summarize_wikipedia_article(url)

# Print the summary
print(summary)
