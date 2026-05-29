import os
from dotenv import load_dotenv
from langsmith import Client, traceable
from openai import OpenAI

load_dotenv()

# LangSmith Client
client = Client(
    api_url=os.getenv("LANGSMITH_ENDPOINT"),
    api_key=os.getenv("LANGSMITH_API_KEY")
)

# OpenAI Client
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

DATASET_NAME = "restaurant_customer_support_dataset_madhuri"


@traceable
def restaurant_chatbot(inputs: dict) -> dict:
    question = inputs["question"]

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful restaurant customer support assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer
    }


def correctness_evaluator(outputs: dict, reference_outputs: dict) -> dict:
    generated = outputs.get("answer", "").lower()
    expected = reference_outputs.get("answer", "").lower()

    score = 1 if generated and expected else 0

    return {
        "key": "correctness",
        "score": score
    }


if __name__ == "__main__":

    experiment_results = client.evaluate(
        restaurant_chatbot,
        data=DATASET_NAME,
        evaluators=[correctness_evaluator],
        experiment_prefix="restaurant-support-gpt4omini"
    )

    print("Evaluation completed!")
    print(experiment_results)