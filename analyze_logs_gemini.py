import os
import requests

GEMINI_API_KEY = "AIzaSyAWCbDcw_rc7qGHXkGwv9xEiXl3Eh6_aBs"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-latest:generateContent?key={GEMINI_API_KEY}"

def analyze_jenkins_log(log_file):
    with open(log_file, 'r') as f:
        log_content = f.read()

    payload = {
        "contents": [
            {"parts": [{"text": f"Analyze this Jenkins log and suggest fixes:\n{log_content}"}]}
        ]
    }

    response = requests.post(GEMINI_ENDPOINT, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    log_path = "last_build.log"
    if os.path.exists(log_path):
        print("\n=== Gemini AI Analysis ===\n")
        print(analyze_jenkins_log(log_path))
    else:
        print(f"Log file {log_path} not found.")
