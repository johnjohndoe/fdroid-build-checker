from unittest import TestCase

from fdroid_build_checker.parsers.recent_changes_html_parser import (
    RecentChangesHtmlParser,
    RecentChange,
)


class TestRecentChangesHtmlParser(TestCase):
    def test_parse(self):
        package_names = [
            "info.metadude",
        ]
        parser = RecentChangesHtmlParser(
            domain_url="https://f-droid.org",
            url="https://f-droid.org/wiki/index.php?title=Special:RecentChanges&days=30&from=&hidebots=0&hideanons=1"
            "&hideliu=1&limit=500",
        )
        recent_changes = parser.parse(package_names)
        if len(recent_changes) > 0:
            for recent_change in recent_changes:
                self.assert_recent_change(recent_change)

    def assert_recent_change(self, recent_change: RecentChange):
        self.assertTrue(recent_change.date != "")
        self.assertTrue(recent_change.time != "")
        self.assertTrue(recent_change.package != "")
        self.assertTrue(recent_change.version_code != "")
        self.assertTrue(recent_change.href != "")
