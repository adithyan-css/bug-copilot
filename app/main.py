import pathway as pw
from pathway_index import build_live_table
from agent import analyze_text
from report_generator import generate_report


def main():
    print("🚀 Bug Copilot starting...")
    print("👀 Watching data/tickets for live updates...\n")

    docs = build_live_table()

    # Long-horizon memory (session-level)
    bug_memory = []

    def on_update(key, row, time, is_addition):
        content = row["content"]

        if is_addition:
            print("📥 New bug ticket detected")
        else:
            print("✏️ Bug ticket updated")

        bug_memory.append(content)

        combined_text = "\n".join(bug_memory)

        print("\n" + "=" * 60)
        print("🧠 LIVE AI BUG COPILOT REPORT")
        print("=" * 60)

        analysis = analyze_text(combined_text)
        print(analysis)

        # Persist long-horizon insight
        report_path = generate_report(analysis)
        print(f"\n📄 Report updated: {report_path}")
        print("=" * 60 + "\n")

    pw.io.subscribe(
        docs,
        on_change=on_update
    )

    pw.run()



if __name__ == "__main__":
    main()
