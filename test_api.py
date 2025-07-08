from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
fine_tuned_model = "ft:gpt-4.1-nano-2025-04-14:jn-formation::Bqy7zRrJ"

response = client.responses.create(
    model=fine_tuned_model,
    input="Mon produit défectueux est-il couvert par une garantie ?"
)

print(response.output_text)