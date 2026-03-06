import requests
import re
from datetime import datetime

# --- CONFIGURATION ---
USERNAME = "CloudSarathi"
# ನೀವು ಟ್ರ್ಯಾಕ್ ಮಾಡಬೇಕಾದ ರೆಪೊಸಿಟರಿಗಳ ಪಟ್ಟಿ
REPOS = [
    "01-Linux-Fundamentals",
    "02-Git-GitHub",
    "into-the-devops"
]

def get_repo_details(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # ದಿನಾಂಕವನ್ನು ಸುಲಭವಾಗಿ ಓದಲು ಫಾರ್ಮ್ಯಾಟ್ ಮಾಡುವುದು
            last_push = datetime.strptime(data['pushed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%b %d, %Y')
            return {
                "name": data['name'],
                "stars": data['stargazers_count'],
                "issues": data['open_issues_count'],
                "update": last_push,
                "url": data['html_url']
            }
    except Exception as e:
        print(f"Error fetching {repo_name}: {e}")
    return None

def generate_markdown_table():
    # ಟೇಬಲ್ ಹೆಡರ್ - ಮಾಡರ್ನ್ ಸ್ಟೈಲ್
    table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n"
    table += "| :--- | :---: | :---: | :--- |\n"
    
    for repo in REPOS:
        details = get_repo_details(repo)
        if details:
            table += f"| [**{details['name']}**]({details['url']}) | {details['stars']} | {details['issues']} | {details['update']} |\n"
    return table

def update_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = ""
        end_marker = ""

        if start_marker in content and end_marker in content:
            new_table = generate_markdown_table()
            # Regular Expression ಬಳಸಿ ಹಳೆಯ ಟೇಬಲ್ ಅನ್ನು ಹೊಸದರೊಂದಿಗೆ ಬದಲಾಯಿಸುವುದು
            pattern = f"{start_marker}.*?{end_marker}"
            replacement = f"{start_marker}\n\n{new_table}\n\n{end_marker}"
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

            with open("README.md", "w", encoding="utf-8") as f:
                f.write(updated_content)
            print("✅ README table updated successfully!")
        else:
            print("❌ Error: Markers not found in README.md")
    except FileNotFoundError:
        print("❌ Error: README.md file not found")

if __name__ == "__main__":
    update_readme()
