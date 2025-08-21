from dotenv import load_dotenv
import os

load_dotenv()  # loader variabler fra .env i projektroden

print("Hej fra .venv!")
print("API_KEY sat?" , bool(os.getenv("API_KEY")))
