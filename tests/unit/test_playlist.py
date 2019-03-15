import unittest

from nico_client.playlist import Playlist
from tests.helper import get_file_content_as_string


class TestPlaylist(unittest.TestCase):
    def test_get_videos(self):
        raw_html = get_file_content_as_string('mylist.html')
        pl = Playlist(html_string=raw_html)
        videos = pl.get_videos()
        self.assertTrue(len(videos) > 0)