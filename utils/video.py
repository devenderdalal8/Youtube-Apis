# utils/video.py

import json
from datetime import datetime

class Video:
    def __init__(self, title="", thumbnail_url="", base_url="", video_url="",
                 video_id="", duration="" ,resolution=None,
                 resolution_list=None, upload_date=None,video_download_url=None):
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.video_url = video_url
        self.video_id = video_id
        self.base_url = base_url
        self.duration = duration
        self.resolution = resolution if resolution is not None else []
        self.resolution_list = resolution_list if resolution_list is not None else {}
        self.upload_date = upload_date if upload_date is not None else datetime.now().isoformat()
        self.video_download_url = video_download_url

    def to_dict(self):
        return self.__dict__

class SearchVideo:
    def __init__(self, title="",  thumbnail_url="", base_url="", video_url="",
                 video_id="", duration="", resolution=None,
                 resolution_list=None, upload_date=None):
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.video_url = video_url
        self.video_id = video_id
        self.base_url = base_url
        self.duration = duration
        self.resolution = resolution if resolution is not None else []
        self.resolution_list = resolution_list if resolution_list is not None else {}
        self.upload_date = upload_date if upload_date is not None else datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__
