from fastapi import FastAPI
from config.llm import llm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def Hello():
    return {"hello":"world"}

class ProjectInput(BaseModel):
    text: str

@app.post("/suggest")
def suggest(data:ProjectInput):
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
        ("human", data.text)
    ]
    result = llm.invoke(messages)
    return {"msg":result.content}