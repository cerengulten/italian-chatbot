import os
from dotenv import load_dotenv
from groq import Groq

# loading API key from .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


client = Groq(api_key=API_KEY)

def get_llama_response(prompt: str):
  """
  Sends prompts to Groq model and returns the chatbot"s response.
  Specify as string. 
  """

  response = client.chat.completions.create(
          model='llama3-8b-8192',
          messages=[
            {"role": "user", "content": prompt}
          ],
          max_tokens= 200
  )
  return response.choices[0].message.content
