import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env

def lambda_handler(event=None, context=None):
    api_key = os.getenv("API_FOOTBALL_KEY")
    if not api_key:
        return {"statusCode": 400, "body": "API key not found in environment variables."}

    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {
        "x-apisports-key": api_key
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if not data.get("response"):
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "No live matches right now."})
        }

    results = []
    for match in data["response"]:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]
        score = f"{match['goals']['home']} - {match['goals']['away']}"
        results.append(f"{home} vs {away} | Score: {score}")

    return {
        "statusCode": 200,
        "body": json.dumps({"matches": results})
    }


if __name__ == "__main__":
    # For local test runs
    result = lambda_handler()
    print(json.dumps(result, indent=2))
