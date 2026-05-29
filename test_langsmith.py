import os
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

client = Client(
    api_url=os.getenv("LANGSMITH_ENDPOINT"),
    api_key=os.getenv("LANGSMITH_API_KEY")
)

print("Endpoint:", os.getenv("LANGSMITH_ENDPOINT"))
print("Connected!")

projects = list(client.list_projects(limit=5))
print(f"Projects found: {len(projects)}")