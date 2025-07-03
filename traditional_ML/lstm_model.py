import os 
import json
import re
from newspaper import Article
import feedparser

def save_article(keyword_path, content, title):
    """
    Sauvegarde le contenu d'un article dans un fichier texte.

    Args:
        keyword_path (str): Répertoire où sauvegarder l'article.
        content (str): Contenu complet de l'article.
        title (str): Titre de l'article.

    Returns:
        str: Chemin complet du fichier enregistré.
    """
    # Nettoyage du titre pour éviter les caractères non valides dans les noms de fichiers
    safe_title = re.sub(r'[^\w\s]', '', title).replace(" ", "_")
    file_name = f"{safe_title}.txt"
    file_path = os.path.join(keyword_path, file_name)

    # Écrire le contenu complet dans un fichier texte
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path

def fetch_article_with_newspaper(article_url):
    """
    Récupère le contenu complet d'un article à partir de son URL en utilisant Newspaper.

    Args:
        article_url (str): URL de l'article.

    Returns:
        str: Contenu complet de l'article ou None si une erreur survient.
    """
    try:
        # Utilisation de newspaper3k pour extraire le contenu de l'article
        article = Article(article_url)
        article.download()
        article.parse()
        return article.text, article.authors
    except Exception as e:
        print(f"Erreur avec Newspaper : {e}")
        return None, None

def fetch_scientific_articles(save_path="corpus/articles_actualite", metadata_file="all_documents.json"):
    """
    Récupère des articles de presse à partir de flux RSS, extrait leur contenu complet, et enregistre les métadonnées.

    Args:
        save_path (str): Répertoire où sauvegarder les articles extraits.
        metadata_file (str): Fichier JSON pour sauvegarder les métadonnées des articles extraits.
    """
    # Charger ou initialiser les métadonnées
    if os.path.exists(metadata_file):
        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
    else:
        metadata = []

    article_id = len(metadata) + 1  # ID unique pour chaque article

    # URLs des flux RSS et leurs catégories correspondantes
    feed_urls = [
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml"
    ]
    categories = ["world", "u.s", "politics", "business", "technology", "sports", "opinion"]

    for i, feed_url in enumerate(feed_urls):
        # Récupérer et analyser le flux RSS
        feed = feedparser.parse(feed_url)

        # Parcourir chaque article du flux RSS
        for entry in feed.entries:
            title = entry.title
            summary = entry.summary  # Utilisation de 'summary' ou 'content' si disponible
            url = entry.link

            if not url:
                print(f"Article {title} ignoré : URL manquant.")
                continue

            try:
                # Récupérer le contenu complet de l'article
                full_content, authors = fetch_article_with_newspaper(url)
                if not full_content:
                    full_content = summary  # Si le contenu complet est introuvable, utiliser le résumé

                # Sauvegarder l'article
                keyword = categories[i]  # Catégorie correspondant au flux RSS
                keyword_path = os.path.join(save_path, keyword)
                os.makedirs(keyword_path, exist_ok=True)

                file_path = save_article(keyword_path, full_content, title)

                # Ajouter les métadonnées
                metadata.append({
                    "id": article_id,
                    "title": title,
                    "author": authors if authors else "Auteur inconnu",
                    "type": "article d'actualites",
                    "categorie": keyword,
                    "file_path": file_path,
                    "url": url
                })
                article_id += 1
            except Exception as e:
                print(f"Erreur lors de l'enregistrement de {title} : {e}")

    # Sauvegarder les métadonnées dans un fichier JSON
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)
    print(f"Les métadonnées des articles ont été enregistrées dans {metadata_file}")

# Application
if __name__ == "__main__":
    fetch_scientific_articles()
