import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "dashboard-workflow.html"


def assert_true(value, message):
    if not value:
        raise AssertionError(message)


def main():
    html = PAGE.read_text(encoding="utf-8")
    required_sections = {
        "what-this-is": "What This Dashboard Is",
        "what-readers-can-do": "What Readers Can Do",
        "workflow": "End-to-End Workflow",
        "selection-logic": "Selection Logic",
        "news-logic": "News Logic",
        "automated-editorial": "Automated vs Editorial",
        "scope-limits": "Data Scope and Limits",
        "quality-controls": "Quality Controls",
        "current-status": "Current Status",
    }
    for section_id, heading in required_sections.items():
        assert_true(f'id="{section_id}"' in html and heading in html, f"missing workflow section: {heading}")
    required_links = (
        "https://shaunayong-playpark.github.io/IBD_Local_Scan/",
        "https://shaunayong-playpark.github.io/IBD_Local_Scan/latest-brief.html",
        "https://shaunayong-playpark.github.io/IBD_Local_Scan/historical-briefs.html",
        "https://shaunayong-playpark.github.io/IBD_Local_Scan/game-tracker.html",
    )
    for href in required_links:
        assert_true(f'href="{href}"' in html, f"missing public dashboard link: {href}")
    assert_true(len(re.findall(r'class="flow-step"', html)) == 9, "workflow should contain nine numbered stages")
    unsupported = ("real-time data", "real-time tracking dashboard", "automatic editorial approval", "automatically approves")
    for phrase in unsupported:
        assert_true(phrase.lower() not in html.lower(), f"unsupported claim found: {phrase}")
    assert_true("Editorial approval is required" in html, "editorial approval must be described as editorial")
    print("DASHBOARD_WORKFLOW_BRIEF_PASS")


if __name__ == "__main__":
    main()
