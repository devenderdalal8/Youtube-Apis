from pytubefix import Playlist
from utils.RateLimiter import RateLimiter
from utils.YoutubeDownloader import YouTubeDownloader
from utils.video import Video

class PlaylistDownloader:
    def __init__(self, url):
        self.playlist = Playlist(url)
        self.rate_limiter = RateLimiter(rate_per_second=3)

    def download_audio(self, video_url, mp3=True):
        yt_downloader = YouTubeDownloader(video_url, cache=self.cache)
        return yt_downloader.download_audio(mp3=mp3)

    def download_all_videos_audio(self, mp3=True):
        tasks = [self.download_audio(video.url, mp3) for video in self.playlist.videos]
        return tasks

    def get_video_details(self, video):
        video_details = Video(
            base_url=video.watch_url,
            title=video.title,
            thumbnail_url=video.thumbnail_url,
            video_id=video.video_id,
            video_url=video.watch_url,
            duration=video.length,
            video_download_url=video.streams.get_highest_resolution()
        )
        return video_details.to_dict()

    def download_complete_playlist(self):
        tasks = [self.get_video_details(video) for video in self.playlist.videos]
        result = {
            "videos": tasks,
            "total": len(self.playlist.videos)
        }
        return result
