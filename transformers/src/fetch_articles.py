import requests
from newspaper import Article
import json
from preprocessing import preprocess_and_vectorize

base_url = "https://content.guardianapis.com/search"
api_key = "test"  # Public API key (no authentication required)
vector_file_path = 'data/processed/documents_vectors.json'
categories = ["culture", "sport", "technology", "science", "health", "world"]

def fetch_and_vectorize_articles():
    with open(vector_file_path, 'a') as vector_file:
        for category in categories:
            page = 1
            total_articles_collected = 0

            while total_articles_collected < 1000:
                params = {
                    "section": category,
                    "page-size": 50,
                    "page": page,
                    "api-key": api_key,
                    "show-fields": "body"
                }
                response = requests.get(base_url, params=params)

                if response.status_code != 200:
                    print(f"Failed to fetch articles for {category}: {response.status_code}")
                    break

                articles = response.json().get("response", {}).get("results", [])

                if not articles:
                    break

                for article in articles:
                    url = article.get("webUrl")
                    try:
                        content = article.get("fields", {}).get("body", "")
                        if not content:
                            news_article = Article(url)
                            news_article.download()
                            news_article.parse()
                            content = news_article.text

                        document_vector = preprocess_and_vectorize(content)

                        vector_entry = {
                            'id': total_articles_collected + 1,
                            'vector': document_vector,
                            'category': category,
                            'url': url
                        }
                        json.dump(vector_entry, vector_file)
                        vector_file.write('\n')

                        total_articles_collected += 1

                        if total_articles_collected >= 1000:
                            break

                    except Exception as e:
                        print(f"Error processing article {url}: {e}")

                page += 1

            print(f"Collected {total_articles_collected} articles for category: {category}")

if __name__ == "__main__":
    fetch_and_vectorize_articles()