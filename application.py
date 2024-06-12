import langchain
import os
from random import randint
from flask import Flask, render_template, request, session, render_template_string
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import MessagesPlaceholder
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_core.messages import AIMessage, HumanMessage
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

application = Flask(__name__)


OPENAI_API_KEY='xxxxxxxxxxxxxxxxxxx'
# os.environ['OPEN_API_KEY'] = OPENAI_API_KEY
LANGCHAIN_TRACING_V2 = True
LANGCHAIN_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
PINECONE_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

chat = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model='gpt-3.5-turbo',
    temperature = 0,
    streaming = True
)

### EMBEDDINGS
## Embedding Techinque of OPENAI
embed_model=OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key = OPENAI_API_KEY )
print(len(embed_model.embed_query('hola')))

# CONNECT TO PINECONE DATABASE

pc=Pinecone(api_key=PINECONE_API_KEY)
index_name = 'eguins'
namespace = "espacio"

vectorstore = PineconeVectorStore(
    pinecone_api_key = PINECONE_API_KEY,
    index_name=index_name,
    embedding=embed_model,
    namespace=namespace,
)
retriever=vectorstore.as_retriever()

# query = "in which companies did ezequiel used to work"
# print(vectorstore.similarity_search(query, k=1))


# Incorporate the retriever into a question-answering chain.
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chat, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    print("session_id", session_id)
    return store[session_id]


conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

def get_completion(usr_txt, session_id):
    conversational_rag_chain.invoke(
        {"input": usr_txt},
        config={
            "configurable": {"session_id": session_id}
        },  # constructs a key "abc123" in `store`.
    )["answer"]
    last_message = store[session_id].messages[-1].content
    return last_message

# print(get_completion('si estamos en mayo del 2024, cuantos años trabajó ezequiel en Paradox?'))

@application.route("/")

def home():
    if 'session_id' not in session:
        session['session_id'] = randint(0, 9999) 
    return render_template("./index.html")
@application.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    session_id = session.get('session_id')
    response = get_completion(userText, session_id) 
     #return str(bot.get_response(userText)) 
    return response

if __name__ == "__main__":
    application.debug = True
    application.run()





