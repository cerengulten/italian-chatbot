from fastapi import FastAPI
from pydantic import BaseModel
from .llm_client import get_llama_response
from .memory import add_message, get_memory_text

app = FastAPI()

class ChatRequest(BaseModel): 
  message: str

@app.get("/health")
def health():
  return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
   
  user_msg = req.message
    

  history = get_memory_text()
  full_prompt = (
    "You are an AI assistant that helps users learn Italian. \n"
    "Always give short explanations and examples. \n\n"
    "Ask users their goals and Italian levels and give response based on these. \n\n"
    + history + 
    f"User: {user_msg}|nBot:"
  )

  bot_response = get_llama_response(full_prompt)

  add_message(user_msg, bot_response)

  return {"reply": bot_response}


