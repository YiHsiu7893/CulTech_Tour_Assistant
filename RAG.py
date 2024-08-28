"""
Model:
https://huggingface.co/taide/TAIDE-LX-7B-Chat-4bit
"""
from huggingface_hub import login
token = "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"
#login(token=token, add_to_git_credential=True)

import warnings
# Ignore future warnings.
warnings.filterwarnings('ignore', category=FutureWarning)

## Import necessary libraries.
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms.llamacpp import LlamaCpp
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate


# Load .pdf document.
loader = PyPDFDirectoryLoader("./Knowledge")
documents = loader.load()
#print(documents)

# Split the whole document into several chunks.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

# Embedding model.
embeddings = HuggingFaceEmbeddings(model_name="ckiplab/bert-base-chinese")

# Convert documents into vector representations.
vectorstore = Chroma.from_documents(chunks, embeddings)

# Retriever.
retriever = vectorstore.as_retriever(search_kwargs={'k': 3})

"""
query = "培桂堂的建築有什麼特色?"
search = vectorstore.similarity_search(query)
print(search[0].page_content)
print(retriever.get_relevant_documents(query))
"""


# Instantiate the LlamaCpp language model.
llm = LlamaCpp(
    model_path= "D:/Downloads/taide-7b-a.2-q4_k_m.gguf",
    temperature=0.3,
    max_tokens=2048,
    top_p=1,
    verbose=False,
    #n_gpu_layers=33,
    n_ctx=1024)


# Define prompt template.
template = """
已知內容: {context}
</s>
你是一位嚮導，請根據以上內容回答以下問題。請勿提供與已知內容無關的資訊。請用「答:」開頭。
</s>
問題: {query}
</s>
回答:
"""

prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever,  "query": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


# A function to call for LLM
def llm_call(sent):
    response = rag_chain.invoke(sent)

    return response.split(": ")[-1]


if __name__ == '__main__':
    query = "培桂堂的建築有什麼特色?"
    print(llm_call(query))