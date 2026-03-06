
import requests
import json

# ನಿಮ್ಮ GitHub ಯೂಸರ್ ನೇಮ್ ಮತ್ತು ನೀವು ಟ್ರ್ಯಾಕ್ ಮಾಡಬೇಕಾದ ರೆಪೊಸಿಟರಿಗಳು
username = "CloudSarathi"
repos = ["01-Linux-Fundamentals", "02-Git-GitHub", "into-the-devops"]

def fetch_repo_info(repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url).json()
    return {
        "name": response.get("name"),
        "stars": response.get("stargazers_count"),
        "issues": response.get("open_issues_count"),
        "update": response.get("pushed_at")[:10] # ದಿನಾಂಕ ಮಾತ್ರ
    }

# ಟೇಬಲ್ ಹೆಡರ್
table_content = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n"
table_content += "| :--- | :--- | :--- | :--- |\n"

for r in repos:
    data = fetch_repo_info(r)
    table_content += f"| [{data['name']}](https://github.com/{username}/{r}) | {data['stars']} | {data['issues']} | {data['update']} |\n"

# README ಫೈಲ್ ಅನ್ನು ಓದಿ, ಟೇಬಲ್ ಅಪ್‌ಡೇಟ್ ಮಾಡಿ
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# ಟ್ರ್ಯಾಕಿಂಗ್ ಮಾರ್ಕರ್ ನಡುವೆ ಟೇಬಲ್ ಸೇರಿಸಿ
start_marker = ""
end_marker = ""

new_readme = readme.split(start_marker)[0] + start_marker + "\n" + table_content + "\n" + end_marker + readme.split(end_marker)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
