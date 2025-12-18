import google.generativeai as genai
import os
# If you need to load environment variables from a .env file, uncomment the next two lines:
# from dotenv import load_dotenv
# load_dotenv()
# Load the API key from the environment variable
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(api_key)
print("API key loaded successfully.")

# Configure the API client
genai.configure(api_key=api_key)
print("API client configured successfully.")
# List available models
models = genai.list_models()
for model in models:
    print(model.name)
