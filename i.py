import google.generativeai as genai

genai.configure(api_key="your_api_key_here")

# List available models
models = genai.list_models()
for model in models:
    print(model.name)
