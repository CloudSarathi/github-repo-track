import requests

USERNAME = "CloudSarathi"
REPOS = ["01-Linux-Fundamentals", "02-Git-GitHub"]

def get_stats(repo):
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    try:
        res = requests.get(url).json()
        if 'name' in res:
            return f"| **{res['name']}** | {res['stargazers_count']} | {res['open_issues_count']} | {res['pushed_at'][:10]} |"
    except:
        pass
    return None

# ಹೊಸ ಡೇಟಾ ತಯಾರಿ
table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :---: | :---: | :--- |\n"
rows = [get_stats(r) for r in REPOS if get_stats(r)]
table += "\n".join(rows)

# ಸಂಪೂರ್ಣ ಹೊಸ ಫೈಲ್ ಕಂಟೆಂಟ್ (ಹಳೆಯದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ತೆಗೆದುಹಾಕಿ ಹೊಸದಾಗಿ ಬರೆಯುವುದು)
new_readme_content = f"""# 📊 Cloud Sarathi Live Repo Tracker

ಈ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ನನ್ನ ಪ್ರಮುಖ ಡೆವೊಪ್ಸ್ ರೆಪೊಸಿಟರಿಗಳನ್ನು ಲೈವ್ ಆಗಿ ಟ್ರ್ಯಾಕ್ ಮಾಡುತ್ತದೆ.

{table}
*ಕೊನೆಯದಾಗಿ ಅಪ್‌ಡೇಟ್ ಆಗಿದ್ದು: {requests.utils.datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme_content)

print("✅ README.md has been reset and updated safely!")
