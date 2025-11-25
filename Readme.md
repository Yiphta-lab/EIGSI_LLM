## ℹ️ Note importante pour les utilisateurs Windows

Ollama n’est pas encore disponible nativement sous Windows.  
Pour exécuter cette application, vous devez d’abord installer **WSL2 (Windows Subsystem for Linux)** avec Ubuntu.  

👉 Guide officiel pour installer WSL : [https://learn.microsoft.com/fr-fr/windows/wsl/install](https://learn.microsoft.com/fr-fr/windows/wsl/install)

# Application RAG avec Ollama et Streamlit

## Fonctionnalités

- 🤖 Utilisation de LLMs locaux via Ollama
- 📚 Base de connaissance vectorielle avec ChromaDB
- 📄 Support pour l'import de documents PDF, TXT et CSV
- 🔍 Recherche sémantique sur les documents importés
- 💬 Interface de chat interactive
- 📊 Gestion et visualisation des documents

## Prérequis

- Python 3.11 ou supérieur
- [Ollama](https://github.com/ollama/ollama) installé et en cours d'exécution

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Yiphta-lab/EIGSI_LLM.git
cd EIGSI_LLM
```

### 2. Configuration de l'environnement

Installez les dépendances à l'aide de uv:

```bash
# Installation de uv si vous ne l'avez pas déjà
pip install uv

# Installation des dépendances
uv sync
```

### 3. Préparation d'Ollama

Assurez-vous qu'Ollama est en cours d'exécution et que vous avez téléchargé les modèles nécessaires:

```bash
# Télécharger un modèle de chat (si ce n'est pas déjà fait)
ollama pull mistral

# Télécharger un modèle d'embeddings (si ce n'est pas déjà fait)
ollama pull nomic-embed-text
```

## Utilisation

### Lancer les exercices

```bash
uv run streamlit run rag_atelier.py
uv run python3 rag_atelier.py
uv run python3 text_to_sql_atelier.py
uv run python3 prompting_atelier.py
uv run python3 assistant_excel_atelier.py
```

## Structure du projet

```sh
EIGSI_LLM/
├── pyproject.toml       # Configuration du projet et dépendances
├── README.md            # Ce fichier
└── rag_atelier.py            # Application Streamlit principale
└── text_to_sql_atelier.py         # Application Streamlit principale
└── prompting_atelier.py         # Application Streamlit principale
└── assistant_excel_atelier.py         # Application Streamlit principale

```
