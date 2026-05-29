import os
import json
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

client = Client(
    api_url=os.getenv("LANGSMITH_ENDPOINT"),
    api_key=os.getenv("LANGSMITH_API_KEY")
)

DATASET_NAME = "restaurant_customer_support_dataset_madhuri_v2"

with open("dataset_examples.json", "r", encoding="utf-8") as f:
    examples = json.load(f)

dataset = client.create_dataset(
    dataset_name=DATASET_NAME,
    description="Custom dataset for evaluating a restaurant customer support chatbot."
)

for example in examples:
    client.create_example(
        inputs=example["inputs"],
        outputs=example["outputs"],
        metadata=example["metadata"],
        dataset_id=dataset.id
    )

print(f"Dataset created successfully: {DATASET_NAME}")
print(f"Total examples uploaded: {len(examples)}")