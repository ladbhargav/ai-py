from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatOllama(
    base_url="https://ollama.com",
    # langchain_ollama expects request headers in client_kwargs
    client_kwargs={
        "headers": {
            "Authorization": f"Bearer {os.getenv("OLLAMA_API_KEY")}"
        }
    },
    model="deepseek-v3.2"
)