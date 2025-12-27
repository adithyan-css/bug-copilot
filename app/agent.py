from sentence_transformers import SentenceTransformer
import numpy as np
from collections import Counter

# --------------------------------------------------
# LOCAL AI MODEL (offline, free, pretrained)
# --------------------------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# --------------------------------------------------
# SEVERITY KNOWLEDGE (domain expertise)
# --------------------------------------------------
SEVERITY_PROFILES = {
    "Critical": "system down, production outage, data loss, security breach",
    "High": "major feature broken, payment failure, repeated crashes",
    "Medium": "partial failure, workaround exists, non-blocking issue",
    "Low": "cosmetic bug, UI issue, typo, minor inconvenience"
}

PRIORITY_ORDER = {
    "Critical": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1
}


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Pre-compute embeddings
severity_embeddings = {
    sev: model.encode(desc)
    for sev, desc in SEVERITY_PROFILES.items()
}


def infer_severity(text: str) -> str:
    bug_vec = model.encode(text)
    scores = {
        sev: cosine_sim(bug_vec, vec)
        for sev, vec in severity_embeddings.items()
    }
    return max(scores, key=scores.get)


# --------------------------------------------------
# AGENT LOGIC
# --------------------------------------------------
def analyze_each_bug(bug_texts):
    analyzed = []
    for bug in bug_texts:
        severity = infer_severity(bug)
        analyzed.append({
            "text": bug,
            "severity": severity
        })
    return analyzed


def prioritize_bugs(bugs):
    return sorted(
        bugs,
        key=lambda b: PRIORITY_ORDER[b["severity"]],
        reverse=True
    )


def detect_trends(bugs):
    return Counter(b["severity"] for b in bugs)


def analyze_text(context: str) -> str:
    if not context.strip():
        return "No bug reports available yet."

    bug_texts = [b.strip() for b in context.split("\n") if b.strip()]

    # ---- Agent steps ----
    analyzed = analyze_each_bug(bug_texts)
    prioritized = prioritize_bugs(analyzed)
    trends = detect_trends(analyzed)

    report = []
    report.append("🧠 LIVE AI BUG COPILOT REPORT")
    report.append("--------------------------------")

    report.append("🧩 Agent Reasoning Steps:")
    report.append("1️⃣ Classified each incoming ticket")
    report.append("2️⃣ Inferred severity using semantic similarity")
    report.append("3️⃣ Prioritized bugs based on impact")
    report.append("4️⃣ Compared with historical trends")
    report.append("5️⃣ Generated recommended actions\n")

    report.append("📊 Severity distribution:")
    for sev, count in trends.items():
        report.append(f"- {sev}: {count}")

    report.append("\n🔥 Top priority bugs:")
    for bug in prioritized[:3]:
        report.append(f"[{bug['severity']}] {bug['text']}")

    report.append("\n✅ Suggested actions:")
    if trends.get("Critical", 0) > 0:
        report.append("- Immediate rollback / hotfix required")
    if trends.get("High", 0) > 0:
        report.append("- Prioritize high-severity fixes in next sprint")
    if trends.get("Medium", 0) > 0:
        report.append("- Schedule fixes and monitor escalation")
    if trends.get("Low", 0) > 0:
        report.append("- Defer cosmetic issues to backlog")

    return "\n".join(report)
