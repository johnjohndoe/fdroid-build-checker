from unittest import TestCase

from fdroid_build_checker.parsers.last_build_html_parser import LastBuildHtmlParser


class TestLastBuildHtmlParser(TestCase):
    def test_parse_success(self):
        parser = LastBuildHtmlParser(
            url="https://f-droid.org/wiki/page/info.metadude.android.fosdem.schedule/lastbuild_81"
        )
        last_build_result = parser.parse()
        self.assertTrue(last_build_result.is_success())

    # def test_parse_failure(self):
    #     parser = LastBuildHtmlParser(
    #         url="https://f-droid.org/wiki/page/info.metadude.android.rc3.schedule/lastbuild_81"
    #     )
    #     last_build_result = parser.parse()
    #     self.assertFalse(last_build_result.is_success())
