import sys
import urllib.error
import urllib.request

from lxml import etree


class LastBuild:
    url: str = ""
    parsed_text: str = ""

    def __init__(self, url: str, parsed_text: str):
        self.url = url
        self.parsed_text = parsed_text

    def is_success(self) -> bool:
        return self.parsed_text == "Build succeeded"

    def __str__(self) -> str:
        return f"{self.is_success()}, '{self.parsed_text}', {self.url}"


class LastBuildHtmlParser:
    """Parser specialized for reading from the F-Droid last build page."""

    def __init__(self, url: str):
        """
        Initializes the parser with the given URL.

        :param url: The URL of the HTML page.
        """
        self.url = url
        try:
            schedule_data = urllib.request.urlopen(url)
            parser = etree.HTMLParser(recover=True)
            tree = etree.parse(schedule_data, parser)
        except (ValueError, urllib.error.HTTPError) as e:
            print(f"Error ({e}) loading file from URL: {url}")
            sys.exit(1)
        self.root = tree.getroot()

    def parse(self) -> LastBuild:
        """
        Parses the last page to retrieve its last build result.
        Returns a LastBuild or throws an exception.
        """
        for build_log_headline in self.root.iter("h2"):
            for child in build_log_headline.getchildren():
                if child.tag == "span" and child.get("id") == "Build_Log":
                    paragraph = build_log_headline.getnext()
                    return LastBuild(self.url, paragraph.text.strip())
        raise Exception(f"Failure parsing HTML from url = '{self.url}'.")


def main():
    parser = LastBuildHtmlParser(
        url="https://f-droid.org/wiki/page/info.metadude.android.fosdem.schedule/lastbuild_81"
    )
    print(parser.parse())

    parser = LastBuildHtmlParser(
        url="https://f-droid.org/wiki/page/info.metadude.android.rc3.schedule/lastbuild_81"
    )
    print(parser.parse())


if __name__ == "__main__":
    main()
