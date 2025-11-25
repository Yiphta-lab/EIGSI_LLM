from langchain_ollama import ______
from langchain_core.prompts import PromptTemplate

# Modèle Ollama
llm_excel = ____(
    model=_,   # .
    temperature=_,    
    max_tokens=_
)

# Prompt pour classifier si l’utilisateur demande un fichier Excel
prompt_excel = PromptTemplate.from_template("""
....
""")

# Chaîne LangChain
chain_excel = ______ | _______


import re

user_prompts = [
    "Génère un Excel avec un tableau d'amortissement pour un prêt de 250 000 € sur 20 ans à un taux de 3,9 %.",
    "Peux-tu me donner sous forme de fichier CSV la liste de tous les présidents Français, avec une colonne pour leur nom, leur prénom et leur date d'élection.",
    "Quel temps fait-il aujourd'hui ?"
]

for p in user_prompts:
    response = chain_excel.invoke({"question": p})
    text = response.content.strip()

    # On nettoie (Mistral peut répondre "YES", "YES.", "\nYES", etc.)
    answer = text.split()[0].replace(".", "").upper()

    print(p)
    print("Demande un fichier Excel :", answer)
    print("-" * 50)



from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate

# Modèle Ollama (par exemple : mistral, mistral:instruct, qwen2.5, llama3.1…)
llm_python = ____(
    model=___,         # change si tu veux
    temperature=___,
    top_p=___,
    top_k=___,
)

prompt_python_code = PromptTemplate.from_template("""....""")

chain_python_code = _____ | _____



import re

# Prompt utilisateur
request = "Peux-tu me donner et sans aller sur internet sous forme de fichier CSV la liste de tous les présidents Français de la 5ème République, avec une colonne pour leur nom, leur prénom et leur date d'élection ?"

# Exécution du chain
pipe_rep = chain_python_code.invoke({"input": request})

# Le contenu renvoyé par Ollama :
raw_output = pipe_rep.content

# Sécurité : suppression éventuelle des blocs markdown
code = re.sub(r"```python", "", raw_output)
code = re.sub(r"```", "", code)
code = code.strip()

print("=== CODE GÉNÉRÉ ===")
print(code)
print("====================")

# Exécution du code Python généré automatiquement
#exec(code)



import re
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Modèle Ollama
llm_short = ___(model=_, temperature=__)
llm_long  = ___(model=___, temperature=___)

def run_query(query: str) -> str:

    	""" """
        return response.content.strip()

print(run_query("Quel est le pays qui dispose de la plus grande superficie de forêts ?"))

run_query("Peux-tu me donner sans aller sur internet sous forme de fichier Excel la liste de tous les présidents Français de la 5ème République, avec une colonne pour leur nom, leur prénom et leur date d'élection ?")
