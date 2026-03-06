import requests

username = "CloudSarathi"
repos = ["01-Linux-Fundamentals", "02-Git-GitHub"] # ನಿಮ್ಮ ರೆಪೊಸಿಟರಿ ಹೆಸರುಗಳು

def fetch_info(repo):
    try:
        url = f"https://api.github.com/repos/{username}/{repo}"
        res = requests.get(url).json()
        return f"| **{res['name']}** | {res['stargazers_count']} | {res['open_issues_count']} | {res['pushed_at'][:10]} |"
    except:
        return f"| {repo} | Error | Error | Error |"

# ಟೇಬಲ್ ತಯಾರಿ
table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :--- | :--- | :--- |\n"
for r in repos:
    table += fetch_info(r) + "\n"

# README ಅಪ್‌ಡೇಟ್
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = ""
end_marker = ""

if start_marker in content and end_marker in content:
    header = content.split(start_marker)[0]
    footer = content.split(end_marker)[1]
    new_readme = header + start_marker + "\n" + table + "\n" + end_marker + footer
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("Dashboard updated successfully!")
else:
    print("Error: Markers not found in README.md!")
    exit(1)
