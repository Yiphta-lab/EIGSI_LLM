from langchain_ollama import ChatOllama

# Initialisation du modèle Ollama (Mistral)
llm = ChatOllama(
    model="mistral",      # ou "mistral:7b-instruct" si instruct
    temperature=0.1,
    base_url="http://localhost:11434"
)

# Question
question = "Quel est l'âge de l'univers ?"

# Prompt clair pour la génération concise
prompt = """"""

# Génération via Ollama
response = llm.invoke(prompt)

# Récupération du texte
output_text = response.content.strip()

# Affichage
print(output_text)



# Prompt clair pour la génération concise
prompt = """"""

# Génération via Ollama
response = llm.invoke(prompt)

# Récupération du texte
output_text = response.content.strip()

# Affichage
print(output_text)




# Few-Shot Prompt : autres exemples pour guider le modèle
prompt = """"""

# Génération via Ollama
response = llm.invoke(prompt)

# Récupération du texte
output_text = response.content.strip()

# Affichage
print(output_text)



# Prompt clair pour la génération concise
prompt = """"""

# Génération via Ollama
response = llm.invoke(prompt)

# Récupération du texte
output_text = response.content.strip()

# Affichage
print(output_text)


# L'instruction à donner au modèle
question = """

J'ai 3 disques dur capables de stocker 500 Go de données chacun.

Quel sera l'espace de stockage total disponible si je rajoute 2 disques durs ?

"""

# On tokenise l'instruction en la mettant tout d'abord dans la template adéquate : instruction-input data-output indicator
prompt = """"""

# On tokenise l'instruction en la mettant tout d'abord dans la template adéquate : instruction-input data-output indicator
prompt = question
# type de prompt:few shot
# Génération via Ollama
llm = ChatOllama(
    model="mistral",      # ou "mistral:7b-instruct" si instruct
    temperature=0.02,
    base_url="http://localhost:11434"
)
response = llm.invoke(prompt)

# Récupération du texte
output_text = response.content.strip()

# Affichage
print(output_text)

llm = ChatOllama(
    model="mistral",      # ou "mistral:7b-instruct" si instruct
    temperature=0.9,
    base_url="http://localhost:11434"
)
response = llm.invoke(prompt)

# Récupération du texte
output_text = response.content.strip()

# Affichage
print(output_text)



