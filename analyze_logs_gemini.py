import os
import requests

# Set your Gemini API key
GEMINI_API_KEY = os.getenv("AIzaSyCNWrqyfeTli_d6ktuH241b5AaAXc9Ue2E")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def analyze_jenkins_log(log_file):
    with open(log_file, 'r') as f:
        log_content = f.read()

    prompt = f"""
    You are a DevOps expert. Analyze this Jenkins build log and provide:
    1. Root cause of failure
    2. Suggested fix steps
    3. Corrected Jenkinsfile snippet if needed

    Jenkins Log:
    {log_content}
    """

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(GEMINI_ENDPOINT, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    log_path = "last_build.log"
    if os.path.exists(log_path):
        analysis = analyze_jenkins_log(log_path)
        print("\n=== Gemini AI Analysis ===\n")
        print(analysis)
    else:
        print(f"Log file {log_path} not found.")