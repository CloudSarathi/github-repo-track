import requests

username = "CloudSarathi"
repos = ["01-Linux-Fundamentals", "02-Git-GitHub"]

def fetch_info(repo):
    try:
        url = f"https://api.github.com/repos/{username}/{repo}"
        res = requests.get(url).json()
        name = res.get('name', repo)
        stars = res.get('stargazers_count', 0)
        issues = res.get('open_issues_count', 0)
        update = res.get('pushed_at', '2026-03-01')[:10]
        return f"| **{name}** | {stars} | {issues} | {update} |"
    except Exception as e:
        return f"| {repo} | Error | Error | Error |"

# ಹೊಸ ಟೇಬಲ್ ತಯಾರಿ
table_header = "| Repository | ⭐ Stars | 🛠️ Issues | 📅 Last Update |\n| :--- | :--- | :--- | :--- |\n"
table_rows = "\n".join([fetch_info(r) for r in repos])
full_table = f"{table_header}{table_rows}"

# README ಅಪ್‌ಡೇಟ್ ಮಾಡುವ ಸುಲಭ ವಿಧಾನ
start_marker = ""
end_marker = ""

try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    if start_marker in content and end_marker in content:
        # ಹಳೆಯ ಡೇಟಾವನ್ನು ಹೊಸ ಟೇಬಲ್‌ನೊಂದಿಗೆ ರಿಪ್ಲೇಸ್ ಮಾಡುವುದು
        import re
        pattern = f"{start_marker}.*?{end_marker}"
        replacement = f"{start_marker}\n\n{full_table}\n\n{end_marker}"
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ Dashboard updated successfully!")
    else:
        print("❌ Markers not found! Please add them to README.md")
        exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
