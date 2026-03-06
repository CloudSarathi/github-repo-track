import requests
from datetime import datetime

# ನಿಮ್ಮ ಯೂಸರ್ ನೇಮ್
USERNAME = "CloudSarathi"

def get_all_repos():
    # ಪಬ್ಲಿಕ್ ರೆಪೊಸಿಟರಿಗಳನ್ನು ಪಡೆಯಲು API Call (ಇತ್ತೀಚಿನ ಅಪ್‌ಡೇಟ್ ಮೊದಲು ಬರುವಂತೆ ಸಾರ್ಟ್ ಮಾಡಲಾಗಿದೆ)
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching repos: {e}")
    return []

def format_row(repo):
    name = repo.get('name')
    url = repo.get('html_url')
    stars = repo.get('stargazers_count', 0)
    issues = repo.get('open_issues_count', 0)
    # ದಿನಾಂಕವನ್ನು ಸುಲಭವಾಗಿ ಓದಲು ಫಾರ್ಮ್ಯಾಟ್ ಮಾಡಿ (YYYY-MM-DD)
    date = repo.get('pushed_at', '')[:10]
    # ಭಾಷೆಯನ್ನು ತೋರಿಸಲು (Python, Shell, etc.)
    lang = repo.get('language', 'No Lang')
    
    return f"| [**{name}**]({url}) | {lang} | ⭐ {stars} | 🛠️ {issues} | 📅 {date} |"

# 1. ಎಲ್ಲಾ ರೆಪೊಸಿಟರಿಗಳ ಡೇಟಾ ಸಂಗ್ರಹ
all_repos = get_all_repos()

# 2. ಟೇಬಲ್ ಹೆಡರ್ ಸಿದ್ಧಪಡಿಸುವುದು
header = "| Repository | Language | Stars | Issues | Last Update |\n| :--- | :--- | :---: | :---: | :--- |\n"

# 3. ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ರೆಪೊಸಿಟರಿಯನ್ನು (CloudSarathi/CloudSarathi) ಹೊರತುಪಡಿಸಿ ಉಳಿದೆಲ್ಲವನ್ನೂ ಸೇರಿಸಿ
rows = [format_row(r) for r in all_repos if r['name'].lower() != USERNAME.lower()]
table = header + "\n".join(rows)

# 4. ಪೂರ್ತಿ README ಕಂಟೆಂಟ್ ತಯಾರಿ
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

readme_content = f"""# 📊 Cloud Sarathi Live Project Dashboard

ನನ್ನ ಕಲಿಕೆ ಮತ್ತು ಡೆವೊಪ್ಸ್ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳ ಲೈವ್ ಅಪ್‌ಡೇಟ್ ಇಲ್ಲಿದೆ. ಇದು ಆಟೋಮ್ಯಾಟಿಕ್ ಆಗಿ ಅಪ್‌ಡೇಟ್ ಆಗುತ್ತದೆ.

{table}
*Last Automated Update: {current_time} (IST)*

---
### 🚀 Connect with Cloud Sarathi
* 📺 [YouTube Channel](https://www.youtube.com/@CloudSarathi)
* 💼 [LinkedIn](https://www.linkedin.com/in/cloudsarathi)
"""

# 5. ಹಳೆಯದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಅಳಿಸಿ ಹೊಸದಾಗಿ ಬರೆಯುವುದು (Overwrite)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"✅ Dashboard updated with {len(rows)} public repositories!")
