from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings


def create_vector_store(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    embeddings = OllamaEmbeddings(
        model="llama3"
    )

    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name="document_rag"
    )

    return vector_store


def ask_document_question(vector_store, question):
    docs = vector_store.similarity_search(question, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model="llama3")

    prompt = f"""
    Answer ONLY from this document.

    Context:
    {context}

    Question:
    {question}
    """

    return llm.invoke(prompt)


def analyze_document_risks(vector_store):
    docs = vector_store.similarity_search(
        "Find legal financial compliance contractual risks",
        k=6
    )

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model="llama3")

    prompt = f"""
    Analyze this document for risks.

    Identify:
    - financial risks
    - legal risks
    - compliance risks
    - privacy concerns
    - contractual issues

    Also suggest mitigation.

    Document:
    {context}
    """

    return llm.invoke(prompt)