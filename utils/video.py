# utils/video.py

import json
from datetime import datetime

class Video:
    def __init__(self, title="", description="", thumbnail_url="", base_url="", video_url="",
                 video_id="", duration="", views="", likes=None, resolution=None,
                 resolution_list=None, upload_date=None, channel_url="", channel_id=""):
        self.title = title
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.video_url = video_url
        self.video_id = video_id
        self.base_url = base_url
        self.duration = duration
        self.views = views
        self.likes = likes  # Can be None
        self.resolution = resolution if resolution is not None else []
        self.resolution_list = resolution_list if resolution_list is not None else {}
        self.upload_date = upload_date if upload_date is not None else datetime.now().isoformat()
        self.channel_url = channel_url
        self.channel_id = channel_id

    def to_dict(self):
        return self.__dict__

class SearchVideo:
    def __init__(self, title="", description="", thumbnail_url="", base_url="", video_url="",
                 video_id="", duration="", views="", likes=None, resolution=None,
                 resolution_list=None, upload_date=None, channel_url="", channel_id=""):
        self.title = title
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.video_url = video_url
        self.video_id = video_id
        self.base_url = base_url
        self.duration = duration
        self.views = views
        self.likes = likes  # Can be None
        self.resolution = resolution if resolution is not None else []
        self.resolution_list = resolution_list if resolution_list is not None else {}
        self.upload_date = upload_date if upload_date is not None else datetime.now().isoformat()
        self.channel_url = channel_url
        self.channel_id = channel_id

    def to_dict(self):
        return self.__dict__
