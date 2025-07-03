import unittest
from src.preprocessing import preprocess_and_vectorize
from src.fetch_articles import fetch_and_vectorize_articles

class TestPreprocess(unittest.TestCase):
    def test_preprocess_and_vectorize(self):
        text = "This is a test sentence."
        vector = preprocess_and_vectorize(text)
        self.assertEqual(len(vector), 768)  # BERT base has 768-dimensional embeddings


class TestFetchArticles(unittest.TestCase):
    def test_fetch_and_vectorize_articles(self):
        # Testez ici que la fonction s'exécute sans erreur
        pass  # À compléter avec des tests spécifiques

if __name__ == "__main__":
    unittest.main()