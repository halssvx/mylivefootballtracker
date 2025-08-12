 Live Football Score Fetcher ⚽

A simple Python script (AWS Lambda-ready) that fetches **live football (soccer) match scores** from the [API-FOOTBALL](https://www.api-football.com/) service using their `fixtures?live=all` endpoint.  

The script uses a `.env` file to securely store your API key and works both locally and in AWS Lambda.

---

## 📌 Features
- Fetches **all live matches** from API-FOOTBALL.
- Displays match details in the format:
Home Team vs Away Team | Score: X - Y

yaml
- Returns a clean JSON response suitable for **API responses**.
- Can run locally or in AWS Lambda.

---

## 🏗 AWS Infrastructure
I also created an **AWS Lambda deployment** using **Terraform** to automate infrastructure provisioning.  
This README focuses **only on the Python side** of the project — the Terraform part is a separate showcase of Infrastructure-as-Code skills.  
- Python script: Handles API request, parsing, and response formatting.
- Terraform: Creates Lambda, IAM roles, and environment variable setup.

---

## 🚀 Setup Instructions

###  Clone the repository

git clone https://github.com/your-username/live-football-scores.git
cd live-football-scores
 Install dependencies

pip install -r requirements.txt
requirements.txt should include:


requests
python-dotenv
3️⃣ Create your .env file
This file stores your API-FOOTBALL key securely.

env
API_FOOTBALL_KEY=your_api_key_here
Note: Never commit .env files to GitHub!
Add .env to your .gitignore:


.env
4️⃣ Run locally
 main.py
Example output:
{
  "statusCode": 200,
  "body": "{\"matches\": [\"Team A vs Team B | Score: 2 - 1\"]}"
}
Deploy to AWS Lambda
Zip your project (including dependencies inside a package folder or use a Lambda layer).

Set the API_FOOTBALL_KEY as an environment variable in your Lambda configuration.

Use lambda_handler as the entry point.

Environment Variables
Variable	Description	Required
API_FOOTBALL_KEY	Your API key from API-FOOTBALL	


🛠 How .env is Used
.env file is loaded at runtime using:

python
from dotenv import load_dotenv
load_dotenv()
The script retrieves the key with:

python
api_key = os.getenv("API_FOOTBALL_KEY")
This approach keeps your API key secure and out of your code.


Author: haalatech
⭐ Star this repo if you found it useful!
