import google.generativeai as genai

genai.configure(api_key="AIzaSyD4OtvXJt5sV29kabzbbfjo5iZnLGcSYs4")

# List available models
models = genai.list_models()
for model in models:
    print(model.name)
