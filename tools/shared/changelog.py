import re
from datetime import datetime
from pathlib import Path


def get_current_version_changelog(changelog_path: Path) -> str:
    sections = [
        section
        for section in changelog_path.read_text().split("\n\n")
        if re.search(r"- \w", section)
    ]
    if sections:
        section = sections[0]
        return "\n".join(
            line for line in section.splitlines() if not line.startswith("#")
        )


def update_changelog_to_new_version(
    changelog: str,
    old_tag: str,
    new_tag: str,
    new_version_name: str,
    stable_branch: str | None = "stable",
    develop_branch: str = "develop",
) -> str:
    if f"[{new_version_name}]" in changelog:
        return changelog
    changelog = re.sub("Unreleased", new_version_name, changelog, count=1)
    changelog = re.sub(stable_branch, old_tag, changelog, count=1)
    changelog = re.sub(develop_branch, new_tag, changelog, count=1)
    changelog = re.sub(
        "××××-××-××", datetime.now().strftime("%Y-%m-%d"), changelog
    )
    changelog = (
        f"## [Unreleased](https://github.com/LostArtefacts/TRX/compare/{stable_branch or new_tag}...{develop_branch}) - ××××-××-××\n\n"
        + changelog
    )
    return changelog
