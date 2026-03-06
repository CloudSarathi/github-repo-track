import requests
from datetime import datetime

USERNAME = "CloudSarathi"

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except:
        return []
    return []

def create_repo_card(repo):
    name = repo.get('name')
    desc = repo.get('description', "No description available.")
    stars = repo.get('stargazers_count', 0)
    forks = repo.get('forks_count', 0)
    issues = repo.get('open_issues_count', 0)
    updated = repo.get('updated_at', '')[:10]
    url = repo.get('html_url')
    topics = repo.get('topics', [])
    
    # ಹ್ಯಾಶ್‌ಟ್ಯಾಗ್ ಸೆಕ್ಷನ್
    tags = " ".join([f"#{t}" for t in topics[:5]]) if topics else "#devops #learning"
    
    # ಕಾರ್ಡ್ ಡಿಸೈನ್ (HTML & Markdown mix)
    card = f"""
📂 **[{name}]({url})**

{desc}

🗓 Last Updated: {updated} | 👤 Author: {USERNAME} | 🏷 Open Issues: {issues}
⭐ Stars: {stars} | 🍴 Forks: {forks} | ⚪ CI/CD Status: ![Status](https://img.shields.io/github/actions/workflow/status/{USERNAME}/{name}/tracker.yml?branch=main&style=flat-square)
{tags}
---
"""
    return card

# 1. ಡೇಟಾ ಪಡೆಯಿರಿ
all_repos = get_repos()

# 2. ಕಾರ್ಡ್‌ಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ (Profile README ಸ್ಕಿಪ್ ಮಾಡಿ)
repo_cards = ""
for r in all_repos:
    if r['name'].lower() != USERNAME.lower():
        repo_cards += create_repo_card(r)

# 3. README ಫಾರ್ಮ್ಯಾಟ್
current_time = datetime.now().strftime('%Y-%m-%d')
readme_content = f"""# 🚀 Cloud Sarathi - My DevOps Portfolio

ನನ್ನ ಎಲ್ಲಾ ಪ್ರಮುಖ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳ ಲೈವ್ ಅಪ್‌ಡೇಟ್ ಮತ್ತು ವಿವರ ಇಲ್ಲಿದೆ.

{repo_cards}
*🔄 Last Automated Sync: {current_time}*
"""

# 4. ಫೈಲ್‌ಗೆ ಬರೆಯಿರಿ
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ Professional UI Dashboard Updated!")
