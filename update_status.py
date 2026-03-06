import requests
import re

USERNAME = "CloudSarathi"
REPOS = ["01-Linux-Fundamentals", "02-Git-GitHub"]

def get_stats(repo):
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    res = requests.get(url).json()
    return f"| **{res.get('name')}** | {res.get('stargazers_count')} | {res.get('open_issues_count')} | {res.get('pushed_at')[:10]} |"

table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :---: | :---: | :--- |\n"
table += "\n".join([get_stats(r) for r in REPOS])

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r".*?"
replacement = f"\n\n{table}\n\n"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
