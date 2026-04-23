from fastapi import FastAPI
from config.llm import llm

app = FastAPI()

@app.get("/")
def Hello():
    return {"hello":"world"}

@app.post("/suggest")
def suggest(text:str):
    messages = [
        (
            "system",
            """You are a project name corrector.

            Fix any spelling, grammar, or sentence errors in the project name the user provides.

            Rules:
            - Return ONLY the corrected project name — nothing else
            - Do not add, remove, or change any meaning
            - Use Title Case
            - If the name is already correct, return it as-is"""
        ),
        ("human", text)
    ]
    result = llm.invoke(messages)
    return result.content