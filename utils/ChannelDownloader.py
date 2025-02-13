
from pytubefix import Channel
from utils.YoutubeDownloader import YouTubeDownloader

class ChannelDownloader:
    def __init__(self, url):
        self.channel = Channel(url)

    def get_channel_name(self):
        return self.channel.channel_name

    def download_all_videos(self):
        results = []
        for video in self.channel.videos:
            yt_downloader = YouTubeDownloader(video.url)
            result = yt_downloader.download_highest_resolution()
            results.append(result)
        return results
