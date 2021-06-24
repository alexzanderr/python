
import unittest
from core.download import *

class TestingDownload(unittest.TestCase):

    def test_download_file_function(self):
        download_url = "https://alexzander.tech/test.mp4"
        dest = r"C:\Users\dragonfire\Downloads"
        names = [
            ("bla1", True),
            ("bla2", True),
            ("bla3", True),
            ("bla4", True),
        ]
        for item in names:
            self.assertEqual(
                download_file(
                    download_url,
                    dest,
                    item[0],
                    open_destination=False,
                    show_progress=item[1]),
                True
            )

    def test_get_yt_video_thumbnail_url_function(self):
        url = "https://www.youtube.com/watch?v=I22AqV9zV50"





if __name__ == '__main__':
    unittest.main()