from datetime import datetime
import os

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)


def generate_report(analysis: str):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report = f"""
==============================
 BUG TREND REPORT
==============================
Generated at: {timestamp}

{analysis}

Notes:
- Report reflects cumulative bug history
- Updates automatically as new tickets arrive
"""

    file_path = f"{REPORT_DIR}/bug_report_{timestamp}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report.strip())

    return file_path
    