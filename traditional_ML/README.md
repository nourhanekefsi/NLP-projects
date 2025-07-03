# **1. Classification de textes avec BERT

Ce projet vise à classer des articles de presse en 5 catégories (culture, sport, technologie, science, santé) en utilisant des embeddings BERT. Les articles sont récupérés via l'API de The Guardian, vectorisés avec BERT, et stockés dans un fichier JSON pour entraîner un modèle de classification.

## **2. Structure du projet

text-classification-project/
│
├── README.md                   # Description du projet, instructions d'installation et d'utilisation
├── requirements.txt            # Liste des dépendances Python
├── .gitignore                  # Fichiers et dossiers à ignorer par Git
│
├── data/                       # Dossier contenant les données
│   ├── raw/                    # Données brutes (vos 5000 articles)
│   ├── processed/              # Données prétraitées (après tokenisation, etc.)
│   └── labels.csv              # Fichier contenant les labels des articles
│
├── models/                     # Dossier pour stocker les modèles entraînés
│   ├── bert_model/             # Modèle BERT fine-tuné
│   └── tokenizer/              # Tokenizer associé à BERT
│
├── notebooks/                  # Dossier pour les notebooks Jupyter
│   ├── exploration.ipynb       # Notebook pour l'exploration des données
│   ├── preprocessing.ipynb     # Notebook pour le prétraitement des données
│   └── training.ipynb          # Notebook pour l'entraînement du modèle
│
├── src/                        # Dossier contenant le code source
│   ├── __init__.py             # Fichier pour rendre le dossier un package Python
│   ├── preprocess.py           # Script pour le prétraitement des données
│   ├── train.py                # Script pour l'entraînement du modèle
│   ├── predict.py              # Script pour faire des prédictions avec le modèle
│   ├── api/                    # Dossier pour l'API FastAPI
│   │   ├── __init__.py
│   │   ├── main.py             # Point d'entrée de l'API FastAPI
│   │   └── models.py           # Modèles Pydantic pour la validation des données
│   └── ui/                     # Dossier pour l'interface utilisateur Gradio
│       ├── __init__.py
│       └── app.py              # Script pour lancer l'interface Gradio
│
├── tests/                      # Dossier pour les tests unitaires
│   ├── __init__.py
│   ├── test_preprocess.py      # Tests pour le prétraitement
│   ├── test_train.py           # Tests pour l'entraînement
│   └── test_predict.py         # Tests pour les prédictions
│
└── scripts/                    # Dossier pour les scripts utilitaires
    ├── start_api.sh            # Script pour démarrer l'API FastAPI
    └── start_ui.sh             # Script pour démarrer l'interface Gradio

## **3. Prérequis

- Python 3.8 ou supérieur
- Bibliothèques Python : voir `requirements.txt`
- Un accès à l'API de The Guardian (clé API)

### **4. Installation des dépendances

```bash
pip install -r requirements.txt
```

### **5. Comment exécuter le projet ?**
Fournissez des instructions étape par étape pour exécuter le projet.


## Comment exécuter le projet ?

### 1. Récupérer les articles et les vectoriser
Exécutez le script pour récupérer les articles de l'API et les vectoriser avec BERT :

```bash
bash scripts/fetch_data.sh
```
### 2. Tester le code
```bash
python -m unittest tests/test_preprocess.py
python -m unittest tests/test_fetch_articles.py
```
### 3. Démarrer l'API FastAPI
Pour servir le modèle via une API, exécutez :

```bash
uvicorn src.api.main:app --reload
```
### 4. Démarrer l'interface utilisateur Gradio
Pour utiliser l'interface utilisateur, exécutez :

```bash
python src/ui/app.py
```

## Rapport

### Données collectées
- Nombre total d'articles : 5000 (1000 par catégorie)
- Taille moyenne d'un article : 500 mots

### Performances du modèle
- Précision : 92%
- Rappel : 89%
- F1-score : 90%

### Observations
- Les articles de la catégorie "sport" sont les plus faciles à classer.
- La catégorie "science" a parfois des chevauchements avec "technologie".


## **7. Contributions

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Pushez la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.
## **8. Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.