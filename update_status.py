import requests
from datetime import datetime

USERNAME = "CloudSarathi"

def get_fancy_font(text):
    # ಇದು ನಾರ್ಮಲ್ ಅಕ್ಷರಗಳನ್ನು Fancy Italic ಅಕ್ಷರಗಳಿಗೆ ಬದಲಾಯಿಸುತ್ತದೆ
    normal_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    fancy_chars  = "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
    mapping = str.maketrans(normal_chars, fancy_chars)
    return text.translate(mapping)

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
    fancy_name = get_fancy_font(name)
    desc = repo.get('description', "No description available.")
    stars = repo.get('stargazers_count', 0)
    forks = repo.get('forks_count', 0)
    issues = repo.get('open_issues_count', 0)
    updated = repo.get('pushed_at', '')[:10]
    url = repo.get('html_url')
    topics = repo.get('topics', [])
    
    tags = " ".join([f"#{t}" for t in topics[:5]]) if topics else "#devops #cloudsarathi"
    
    # ಇಲ್ಲಿ <sub> ಟ್ಯಾಗ್ ಬಳಸುವುದರಿಂದ ಫಾಂಟ್ ಸೈಜ್ ಕಡಿಮೆಯಾಗುತ್ತದೆ ಮತ್ತು ಲೆಟರ್ ಸ್ಪೇಸಿಂಗ್ ನೀಟಾಗಿ ಕಾಣುತ್ತದೆ
    card = f"""
📂 **[{fancy_name}]({url})**

{desc}

<sub>🗓 **Last Updated:** {updated} | 👤 **Author:** {USERNAME} | 🏷 **Open Issues:** {issues}</sub>
<sub>⭐ **Stars:** {stars} | 🍴 **Forks:** {forks} | ⚪ **CI/CD Status**</sub>

<sub>{tags}</sub>
---
"""
    return card

# 1. ಡೇಟಾ ಸಂಗ್ರಹ
all_repos = get_repos()

# 2. ಕಾರ್ಡ್ ಸಿದ್ಧಪಡಿಸಿ
repo_cards = ""
for r in all_repos:
    if r['name'].lower() != USERNAME.lower():
        repo_cards += create_repo_card(r)

# 3. README ಫಾರ್ಮ್ಯಾಟ್
current_time = datetime.now().strftime('%Y-%m-%d')
readme_content = f"""# 🚀 Cloud Sarathi - DevOps Portfolio

{repo_cards}
*🔄 Last Automated Sync: {current_time}*
"""

# 4. ಫೈಲ್‌ಗೆ ಬರೆಯಿರಿ
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ Professional UI with Fancy Font Updated!")
