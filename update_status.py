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

# ಕೇವಲ ಒಂದು ಬಾರಿ ಮಾತ್ರ ಹೆಡರ್ ಸೃಷ್ಟಿಸುವುದು
table = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :---: | :---: | :--- |\n"
stats_list = [get_stats(r) for r in REPOS if get_stats(r) is not None]
table += "\n".join(stats_list)

# README ಓದುವುದು
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# ಹಳೆಯದನ್ನು ಪೂರ್ತಿಯಾಗಿ ರಿಪ್ಲೇಸ್ ಮಾಡಲು Regular Expression ಬಳಕೆ
start_marker = ""
end_marker = ""

# ಮಾರ್ಕರ್ ನಡುವೆ ಇರುವ ಎಲ್ಲವನ್ನೂ (ಹಳೆಯ ಟೇಬಲ್‌ಗಳನ್ನು) ಅಳಿಸಿ ಹೊಸ ಟೇಬಲ್ ಹಾಕುವುದು
pattern = f"{start_marker}.*?{end_marker}"
replacement = f"{start_marker}\n\n{table}\n\n{end_marker}"

if start_marker in content and end_marker in content:
    # DOTALL ಫ್ಲ್ಯಾಗ್ ಬಳಸಿ ಮಲ್ಟಿಪಲ್ ಲೈನ್ಸ್ ಅಪ್‌ಡೇಟ್ ಮಾಡುವುದು
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ Fixed! Table cleaned and updated.")
else:
    print("❌ Markers not found!")
