# Day 3 LangSmith Evaluation Lab - Madhuri

## Domain

Restaurant Customer Support

## Project Overview

This project creates a custom LangSmith evaluation dataset for a restaurant customer support chatbot.

The goal is to evaluate how well an LLM can answer realistic restaurant customer questions such as reservations, allergen inquiries, complaints, delivery questions, refunds, menu recommendations, and customer feedback.

## Dataset

Dataset name:

`restaurant_customer_support_dataset_madhuri`

The dataset contains 10 examples with:

- customer question
- expected answer
- category metadata
- difficulty metadata

## Files

| File | Purpose |
|---|---|
| domain_selection.md | Documents the chosen domain and dataset rationale |
| dataset_examples.json | Contains the 10 dataset examples |
| langsmith_dataset.py | Creates/uploads the dataset to LangSmith |
| evaluation.py | Runs the LangSmith evaluation experiment |
| evaluation_summary.md | Summarizes the evaluation results |
| screenshots/ | Contains LangSmith result screenshots |

## How to Run

Install dependencies:

```bash
pip install langsmith openai python-dotenv