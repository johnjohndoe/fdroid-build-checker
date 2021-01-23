import sys
import urllib.error
import urllib.request
from typing import Dict, List

from lxml import etree


class RecentChange:
    date: str = ""
    time: str = ""
    package: str = ""
    version_code: str = "None"
    href: str = ""

    def __init__(
        self, date: str, time: str, package: str, version_code: str, href: str
    ):
        self.date = date
        self.time = time
        self.package = package
        if version_code is not None and version_code != "":
            self.version_code = version_code
        self.href = href

    def is_redirect(self) -> bool:
        return self.version_code == "None"

    def __str__(self) -> str:
        return f"{self.date}, {self.time}, {self.package}, {self.version_code}, {self.href}"


def destructure_link_text(link_text: str) -> Dict[str, str]:
    """
    Returns a dictionary containing a package and a version code value.
    """
    components = dict()
    parts = link_text.split("/lastbuild")
    components["package"] = parts[0].strip()
    if len(parts) == 2:
        components["version_code"] = parts[1].strip()
    else:
        components["version_code"] = ""
    return components


class RecentChangesHtmlParser:
    """Parser specialized for reading from the F-Droid recent changes page."""

    def __init__(self, domain_url: str, url: str):
        """
        Initializes the parser with the given URL.

        :param domain_url: The domain part with protocol of the url.
        :param url: The URL of the HTML page.
        """
        self.domain_url = domain_url
        try:
            schedule_data = urllib.request.urlopen(url)
            parser = etree.HTMLParser(recover=True)
            tree = etree.parse(schedule_data, parser)
        except (ValueError, urllib.error.HTTPError) as e:
            print(f"Error ({e}) loading file from URL: {url}")
            sys.exit(1)
        self.root = tree.getroot()

    def parse(self, package_names: List[str]) -> List[RecentChange]:
        """
        Parses the rows for the given package names and returns a list of RecentChange.
        The returned list might be empty if no rows are present on the page.
        """
        recent_changes = []

        for changes_list_div in self.root.iter("div"):
            if changes_list_div.get("class") == "mw-changeslist":
                date = ""
                for child in changes_list_div.getchildren():
                    if child.tag == "h4":
                        date = child.text.strip()
                    if child.tag == "div":

                        for table in child.iter("table"):
                            table_classes = table.get("class")
                            if (
                                "mw-enhanced-rc" in table_classes
                                and "mw-changeslist-line-not-watched" in table_classes
                            ):

                                time_stamp = ""
                                for tr in table.iter("tr"):
                                    # print(etree.tostring(tr, method="html", pretty_print=True))

                                    for td in tr.iter("td"):
                                        if td.get("class") == "mw-enhanced-rc":
                                            # print(etree.tostring(td, method="html", pretty_print=True))
                                            for abbr in td.iter("abbr"):
                                                time_stamp = abbr.tail.strip()

                                        for span in td.iter("span"):
                                            # print(etree.tostring(span, method="html", pretty_print=True))
                                            if span.get("class") == "mw-title":

                                                for a in span.iter("a"):
                                                    href = a.get("href")
                                                    # print(etree.tostring(a, method="html", pretty_print=True))
                                                    if (
                                                        a.get("class")
                                                        == "mw-changeslist-title"
                                                    ):
                                                        for (
                                                            package_name
                                                        ) in package_names:
                                                            link_text = a.text.strip()
                                                            if (
                                                                package_name
                                                                in link_text
                                                            ):
                                                                (
                                                                    package,
                                                                    version_code,
                                                                ) = destructure_link_text(
                                                                    link_text
                                                                ).values()
                                                                recent_change = RecentChange(
                                                                    date=date,
                                                                    time=time_stamp,
                                                                    package=package,
                                                                    version_code=version_code,
                                                                    href=f"{self.domain_url}{href}",
                                                                )
                                                                recent_changes.append(
                                                                    recent_change
                                                                )
        return recent_changes


def main():
    package_names = [
        "info.metadude",
    ]
    parser = RecentChangesHtmlParser(
        domain_url="https://f-droid.org",
        url="https://f-droid.org/wiki/index.php?title=Special:RecentChanges&days=30&from=&hidebots=0&hideanons=1"
        "&hideliu=1&limit=500",
    )
    recent_changes = parser.parse(package_names)
    print(*recent_changes, sep="\n")


if __name__ == "__main__":
    main()
