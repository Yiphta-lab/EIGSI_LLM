from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="mistral",      
    temperature=0.1,
    base_url="http://localhost:11434"
)


question = "Quel est l'âge de l'univers ?"


prompt = """"""


response = llm.invoke(prompt)


output_text = response.content.strip()


print(output_text)




prompt = """"""


response = llm.invoke(prompt)


output_text = response.content.strip()


print(output_text)





prompt = """"""


response = llm.invoke(prompt)


output_text = response.content.strip()


print(output_text)




prompt = """"""


response = llm.invoke(prompt)


output_text = response.content.strip()


print(output_text)



question = """

J'ai 3 disques dur capables de stocker 500 Go de données chacun.

Quel sera l'espace de stockage total disponible si je rajoute 2 disques durs ?

"""


prompt = """"""


prompt = question

llm = ChatOllama(
    model="mistral",      
    temperature=0.02,
    base_url="http://localhost:11434"
)
response = llm.invoke(prompt)


output_text = response.content.strip()


print(output_text)

llm = ChatOllama(
    model="mistral",     
    temperature=0.9,
    base_url="http://localhost:11434"
)
response = llm.invoke(prompt)


output_text = response.content.strip()


print(output_text)



