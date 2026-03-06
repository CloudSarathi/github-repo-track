import requests
import re

USERNAME = "CloudSarathi"
# ನಿಮ್ಮ ರೆಪೊಸಿಟರಿ ಹೆಸರುಗಳು ಸರಿಯಾಗಿವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
REPOS = ["01-Linux-Fundamentals", "02-Git-GitHub"]

def get_stats(repo):
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        res = response.json()
        name = res.get('name', repo)
        stars = res.get('stargazers_count', 0)
        issues = res.get('open_issues_count', 0)
        pushed_at = res.get('pushed_at', "0000-00-00")[:10]
        return f"| **{name}** | {stars} | {issues} | {pushed_at} |"
    else:
        print(f"⚠️ Warning: Repository '{repo}' not found or error occurred.")
        return None

# ಲಭ್ಯವಿರುವ ರೆಪೊಸಿಟರಿಗಳ ಡೇಟಾವನ್ನು ಮಾತ್ರ ಸಂಗ್ರಹಿಸುವುದು
stats_list = []
for r in REPOS:
    stat = get_stats(r)
    if stat:
        stats_list.append(stat)

table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :---: | :---: | :--- |\n"
table += "\n".join(stats_list)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r".*?"
replacement = f"\n\n{table}\n\n"

if "" in content:
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ Successfully updated README.md")
else:
    print("❌ Error: Markers not found in README.md")
