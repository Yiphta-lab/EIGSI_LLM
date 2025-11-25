import sqlite3

conn = sqlite3.connect("chinook.db")

def get_full_schema() -> str:
    schema = ""
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master")
    for r in cursor.fetchall():
        schema += (r[0] + "\r\n") if r[0] is not None else ""
    cursor.close()
    return schema

print(get_full_schema())

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="mistral",                 # modèle Ollama installé localement
    base_url="http://localhost:11434",
    temperature=0.3
)



import re
from langchain_ollama import ChatOllama

def text_to_sql(query: str) -> str:
    """Transforme une requête en langage naturel vers une requête SQL via Ollama."""
    
    #

    return sql_query


# Exemple d’appel
print(text_to_sql("Combien y a-t-il d'albums ?"))
def execute_sql(query: str) -> str:
    result = []
    cursor = conn.cursor()
    cursor.execute(query)
    for r in cursor.fetchall():
        result.append(r)
    cursor.close()
    return result

print(execute_sql("SELECT COUNT(*) FROM Album;"))
import re
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model=___,   # Le modèle que tu as déjà téléchargé avec : ollama pull mistral
    temperature=___,
    top_p=___,
    top_k=___
)

def format_sql_response(query: str, result: str) -> str:
    """
    Formatte une réponse SQL de manière lisible via le modèle Ollama (Mistral).
    """

    #

    return cleaned


print(format_sql_response("Combien y a-t-il d'albums ?", "[(347,)]"))


def run_query(query: str) -> str:
    #
    return format_sql_response(query, str(sql_result))


print(run_query("Combien y a-t-il d'albums ?"))
print(run_query("Quelle est la date de la facture la plus récente ?"))
