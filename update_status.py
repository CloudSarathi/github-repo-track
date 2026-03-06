import requests
import re

USERNAME = "CloudSarathi"
REPOS = ["01-Linux-Fundamentals", "02-Git-GitHub"]

def get_stats(repo):
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            res = response.json()
            return f"| **{res.get('name')}** | {res.get('stargazers_count')} | {res.get('open_issues_count')} | {res.get('pushed_at')[:10]} |"
    except:
        pass
    return None

# ಹೊಸದಾಗಿ ಟೇಬಲ್ ರೆಡಿ ಮಾಡಿ
table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :---: | :---: | :--- |\n"
stats_list = [get_stats(r) for r in REPOS if get_stats(r) is not None]
table += "\n".join(stats_list)

# README ಓದಿ
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# ಅತೀ ಮುಖ್ಯ: ಹಳೆಯ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಅನ್ನು ಹುಡುಕಿ ಕ್ಲೀನ್ ಮಾಡುವ ಲಾಜಿಕ್
start_marker = ""
end_marker = ""

# ಇಲ್ಲಿ ನಾವು ಪೂರ್ತಿ ಮಾರ್ಕರ್ ನಡುವಿನ ಭಾಗವನ್ನು ಬದಲು ಮಾಡುತ್ತೇವೆ
# ಒಂದು ವೇಳೆ ಮಲ್ಟಿಪಲ್ ಮಾರ್ಕರ್ಸ್ ಇದ್ದರೆ ಅವೆಲ್ಲವನ್ನೂ ಇದು ಸರಿಪಡಿಸುತ್ತದೆ
new_content = re.sub(
    f"{start_marker}.*?{end_marker}",
    f"{start_marker}\n\n{table}\n\n{end_marker}",
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ Cleanup complete! README is now clean and updated.")
