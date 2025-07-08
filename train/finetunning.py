from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_FILE_ID = os.getenv("OPENAI_FILE_ID")
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"
print("Using training file ID:", OPENAI_FILE_ID)

client = OpenAI()

ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model="gpt-4.1-nano-2025-04-14"
)

# Notez absolument le modèle fine-tuné, il sera nécessaire pour l'utilisation du modèle fine-tuné
try:
    ft_job = client.fine_tuning.jobs.create(
        training_file=OPENAI_FILE_ID,
        model=OPENAI_MODEL
    )
    # Affiche l'id du job (vérifie si l'attribut existe)
    job_id = getattr(ft_job, "id", None)
    if job_id:
        print("Fine Tune Job has been created with id", job_id)
    else:
        print("Fine Tune Job created but no id found:", ft_job)
except Exception as e:
    print("Error creating fine tune job:", e)