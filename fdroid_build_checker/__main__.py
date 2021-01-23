from typing import List

from fdroid_build_checker.parsers.last_build_html_parser import (
    LastBuild,
    LastBuildHtmlParser,
)
from fdroid_build_checker.parsers.recent_changes_html_parser import (
    RecentChange,
    RecentChangesHtmlParser,
)


def parse_recent_change(package_names: List[str]) -> List[RecentChange]:
    parser = RecentChangesHtmlParser(
        domain_url="https://f-droid.org",
        url="https://f-droid.org/wiki/index.php?title=Special:RecentChanges&days=30&from=&hidebots=0&hideanons=1"
        "&hideliu=1&limit=500",
    )
    return parser.parse(package_names)


def print_result(recent_change: RecentChange, last_build: LastBuild) -> None:
    print(f"{recent_change}\n{last_build}")


def main():
    package_names = [
        "info.metadude",
    ]
    recent_changes = parse_recent_change(package_names)
    for recent_change in recent_changes:
        if not recent_change.is_redirect():
            last_build = LastBuildHtmlParser(recent_change.href).parse()
            print_result(recent_change, last_build)


if __name__ == "__main__":
    main()
