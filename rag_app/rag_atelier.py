import os
import uuid
import ollama
import pandas as pd
import streamlit as st
# Imports de LangChain
from langchain.text_splitter import """___________________"""   # Classe qui découpe le texte en "chunks"
from langchain_community.document_loaders import """________""", """________""", """_________"""  
# Trois loaders différents : un pour PDF, un pour CSV, un pour fichiers texte simples

from langchain_community.vectorstores import """______"""   # Base de données vectorielle qu’on utilise dans ce projet
from langchain_ollama import """________""", """__________"""  
# Le premier pour créer les embeddings, le second pour gérer le modèle de chat

# Configuration et constantes (Laissées complètes pour l'initialisation)
OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_EMBEDDING_MODEL = "_______"   # Nom du modèle utilisé pour générer les embeddings
DEFAULT_CHAT_MODEL = "_________"      # Nom du modèle de chat utilisé pour la génération de réponses
TEMP_DIR = "temp_docs"
DB_DIR = "_________"                  # Répertoire où sera stockée la base vectorielle


# Création des dossiers temporaires s'ils n'existent pas
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

# Configuration de la page Streamlit (Laissée complète)
st.set_page_config(page_title="RAG avec Ollama", layout="wide")

# Initialisation des sessions states (Laissée complète)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "document_list" not in st.session_state:
    st.session_state.document_list = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Chat"

# Fonction pour obtenir la liste des modèles disponibles (Laissée complète)
@st.cache_data(ttl=300)
def get_available_models():
    try:
        models = ollama.list()
        model_list = models.get("models", [])
        model_names = [model["model"] for model in model_list]
        chat_models = [model for model in model_names if "embed" not in model.lower()]
        embedding_models = [model for model in model_names if "embed" in model.lower()]
        if not chat_models:
            chat_models = [DEFAULT_CHAT_MODEL]
        if not embedding_models:
            embedding_models = [DEFAULT_EMBEDDING_MODEL]
        return chat_models, embedding_models
    except Exception as e:
        st.error(f"Erreur lors de la récupération des modèles : {e}")
        return [DEFAULT_CHAT_MODEL], [DEFAULT_EMBEDDING_MODEL]

# Fonction pour changer de page (Laissée complète)
def change_page(page):
    st.session_state.selected_page = page

# ----------------------------------------------------------------------
# ATELIER 1 : L’Ingestion de Documents 
# ----------------------------------------------------------------------
def process_uploaded_file(uploaded_file):
    # Créer un nom de fichier unique
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    unique_filename = f"{str(uuid.uuid4())}{file_extension}"
    temp_file_path = os.path.join(TEMP_DIR, unique_filename)

    # Enregistrer le fichier temporairement (Complété)
    with open(temp_file_path, "wb") as f: 
        f.write(uploaded_file.getbuffer())

    # Choisir le bon loader en fonction de l'extension 
    if file_extension == ".pdf":
        loader = "__________" 
    elif file_extension == ".csv":
        loader = "__________" 
    else: # Par défaut, utiliser TextLoader pour .txt et autres
        loader = "__________" 

    # Charger et découper le document
    documents = "__________" 
    text_splitter = "__________" 
    chunks = "__________" 

    # Ajouter le document à la liste avec ses métadonnées 
    doc_info = {
        "filename": uploaded_file.name, "path": temp_file_path, "chunks": len(chunks),
        "size": uploaded_file.size, "id": unique_filename,
    }
    st.session_state.document_list.append(doc_info)

    return chunks

# ----------------------------------------------------------------------
# ATELIER 2 : Création de la Base de Connaissances 
# ----------------------------------------------------------------------
# Fonction pour initialiser/mettre à jour la base de connaissances vectorielle
def update_vectorstore(chunks=None):
    embedding_model = st.session_state.embedding_model

    # Initialiser les embeddings
    embeddings = "___________"

    # Si le vectorstore existe déjà, ajouter les nouveaux chunks
    if st.session_state.vectorstore is not None and chunks:
        st.session_state.vectorstore.add_documents(chunks)
    # Sinon, créer une nouvelle vectorstore
    elif chunks:
        st.session_state.vectorstore = """___________"""
        
    # Si le vectorstore n'existe pas et qu'il n'y a pas de chunks, initialiser une vectorstore vide
    elif st.session_state.vectorstore is None:
        # Créer une collection vide
        st.session_state.vectorstore = """_____________"""


# ----------------------------------------------------------------------
# ATELIER 3 : Le Pipeline de Réponse 
# ----------------------------------------------------------------------
def generate_response_stream(query):

    """Renvoie un générateur de tokens pour permettre le streaming de la réponse."""
    # Récupérer les documents pertinents
    if st.session_state.vectorstore is None:
        llm = """______________"""
        
        return llm.stream(query)

    # Mode RAG (on récupère des chunks depuis le retriever)

    # 1. Créer le retriever (k=4) 
    retriever = "__________" 

    # 2. Récupérer les documents pertinents
    docs = "__________" 

    # Stocker l’info sur les chunks utilisés 
    st.session_state.used_chunks = docs

    # 3. Construire le contexte 
    context = "__________" 

    # 4. Construire le prompt augmenté 
    prompt = "__________" 

    # 5. Instancier le LLM en mode streaming  
    llm = """______________"""

    return  """__________""" 


# ----------------------------------------------------------------------
# ATELIER 4 : Assemblage de l’Interface Streamlit 
# ----------------------------------------------------------------------
def main():

    # Sidebar (Laissé complet pour l'affichage de la structure) 
    with st.sidebar:
        st.title("Configuration RAG")

        # Navigation
        st.subheader("Navigation")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Chat", use_container_width=True):
                change_page("Chat")
        with col2:
            if st.button("Documents", use_container_width=True):
                change_page("Documents")

        st.divider()

        # Sélection des modèles
        chat_models, embedding_models = get_available_models()

        st.subheader("Modèles")
        st.session_state.chat_model = st.selectbox(
            "Modèle de conversation",
            options=chat_models,
            index=chat_models.index(DEFAULT_CHAT_MODEL) if DEFAULT_CHAT_MODEL in chat_models else 0,
        )

        st.session_state.embedding_model = st.selectbox(
            "Modèle d'embeddings",
            options=embedding_models,
            index=embedding_models.index(DEFAULT_EMBEDDING_MODEL) if DEFAULT_EMBEDDING_MODEL in embedding_models else 0,
        )

        st.divider()

        # Upload de documents
        st.subheader("Ajouter des documents")
        uploaded_file = st.file_uploader("Choisir un fichier", type=["pdf", "txt", "csv"])

        if uploaded_file is not None and st.button("Traiter le document", use_container_width=True):
            with st.spinner("Traitement du document en cours..."):
                chunks = "__________" 
                "__________" 
                st.success(f"Document '{uploaded_file.name}' ajouté avec succès!")

    # Page principale  
    if st.session_state.selected_page == "Chat":
        render_chat_page()
    else:
        render_documents_page()

# Page de chat
def render_chat_page():
    st.title("Chat RAG avec Ollama")
    # Bouton "Nouvelle Conversation"
    if st.button("Nouvelle Conversation", type="primary"):
        st.session_state.chat_history = []
        st.rerun()

    # Afficher l'historique des messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Zone de saisie pour le chat
    if prompt := st.chat_input("Posez votre question..."):
        # Ajouter le message utilisateur à l'historique
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # Afficher le message utilisateur
        with st.chat_message("user"):
            st.write(prompt)

        # Générer et afficher la réponse
        with st.chat_message("assistant"), st.spinner("Génération de la réponse..."):
            response = st.write_stream("__________")
        # Affichage des chunks utilisés
        if "used_chunks" in st.session_state and st.session_state.used_chunks:
            with st.expander("Chunks utilisés"):
                for idx, doc in enumerate(st.session_state.used_chunks, start=1):
                    st.write(f"**Chunk {idx} :** {doc.page_content[:300]}...")

        # Ajouter la réponse à l'historique
        st.session_state.chat_history.append({"role": "assistant", "content": response})

# Page de documents
def render_documents_page():
    st.title("Documents dans la base de connaissances")

    if not st.session_state.document_list:
        st.info("Aucun document n'a été ajouté. Utilisez le panneau de gauche pour ajouter des documents.")
    else:
        # Créer un DataFrame pour afficher les documents
        doc_data = []
        for doc in st.session_state.document_list:
            doc_data.append(
                {
                    "Nom": doc["filename"],
                    "Taille (Ko)": round(doc["size"] / 1024, 2),
                    "Chunks": doc["chunks"],
                    "ID": doc["id"],
                }
            )

        df = pd.DataFrame(doc_data)
        st.dataframe(df, use_container_width=True)

        # Option pour supprimer tous les documents
        if st.button("Supprimer tous les documents", type="secondary"):
            st.session_state.document_list = []
            st.session_state.vectorstore = None
            for file in os.listdir(TEMP_DIR):
                os.remove(os.path.join(TEMP_DIR, file))
            st.success("Tous les documents ont été supprimés!")
            st.rerun()

if __name__ == "__main__":
    main()
