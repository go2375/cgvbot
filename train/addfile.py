from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment")

INPUT_FILE = "train.jsonl"

client = OpenAI()

file = client.files.create(
  file=open(INPUT_FILE, "rb"),
  purpose="fine-tune"
)

# notez absolument l'id du fichier, il sera nécessaire pour le fine-tuning
print("File has been uploaded to OpenAI with id ", file.id)
