# test_chat.py

from rag_pipeline import load_rag_chain
import re

qa = load_rag_chain()


while True:
    query = input("Ask about your college: \n\n")
    if query.lower() in ["exit", "quit"]:
        break
    print('Invoking model')
    response = qa.invoke(query)
    answer = response['result']
    #sentences = re.split(r'[.?!]', answer)
    #short_answer = sentences[0].strip() + '.'
    print("🤖 Bot:", answer)

