#!/usr/bin/env python3
"""Small live-research validator; historical portfolio checks deliberately retired."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    files = [
        "AGENTS.md", "README.md", "authoritative/START_HERE.md",
        "authoritative/STATE.json", "research/VERSION_BRIDGE.md",
        "research/SOURCE_REGISTER.md", "research/WORKING_PROOF.md",
        "sessions/NEXT_SESSION.md", "scripts/shift_sanity.py",
    ]
    for name in files:
        assert (ROOT / name).is_file(), name
    state = json.loads((ROOT / "authoritative/STATE.json").read_text())
    assert state["schema"] == 2
    assert state["repository"] == "jfairfaxball-348/sunflower-structures-programme"
    assert state["mode"] == "SINGLE_REPOSITORY_DIRECT_MATHEMATICAL_RESEARCH"
    assert state["focus"] == "MISHRA_ARXIV_2606_02667_V1_V2_GAP"
    assert not state["full_conjecture_proved"]
    assert not state["legacy_hierarchy_active"]
    assert not state["legacy_hard_stop_active"]
    assert state["active_next_prompt"] == "sessions/NEXT_SESSION.md"
    for v in ("v1", "v2"):
        assert f"2606.02667{v}" in state["source_versions"][v]
    handoff = (ROOT / state["active_next_prompt"]).read_text()
    assert "NEXT DIRECT RESEARCH INVESTIGATION" in handoff
    assert "full Erdős" in handoff
    assert "C_s" in handoff
    assert "NO S011" not in handoff
    assert "FULL-shift" in handoff or "FULL-shift".lower() in handoff.lower()
    assert "original" in handoff.lower()
    assert "P(s-1,k)" in handoff
    assert "impossible" in (ROOT / "research/VERSION_BRIDGE.md").read_text().lower()
    assert "source" in (ROOT / "research/SOURCE_REGISTER.md").read_text().lower()
    from shift_sanity import main as check_examples
    check_examples()
    print("PASS: active research charter, exact source versions, conjecture integrity and direct next prompt")


if __name__ == "__main__":
    main()
