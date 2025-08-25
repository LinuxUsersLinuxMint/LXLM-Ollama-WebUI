#from ollama import ChatResponse, chat
import subprocess
def load_model(model_name, msg):
    """messages = [
        {
            "role": "user",
            "content": msg
        },
    ]
    response: ChatResponse = chat(model=model_name, messages=messages)
    return response.message.content"""
    model_response = subprocess.run(["ollama", "run", model_name, msg], capture_output=True, text=True, encoding="utf-8")
    model_response = model_response.stdout.strip()
    return model_response