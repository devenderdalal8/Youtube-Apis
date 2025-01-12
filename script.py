from utils.YoutubeDownloader import YouTubeDownloader
from utils.PlaylistDownloader import PlaylistDownloader
from utils.ChannelDownloader import ChannelDownloader
from utils.YoutubeSearch import YouTubeVideoFetcher
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url):
    downloader = YouTubeDownloader(url)
    return downloader.download_highest_resolution()

def video_details(url):
    downloader = YouTubeDownloader(url)
    return downloader.video_details()

def video_resolution(url, resolution):
    downloader = YouTubeDownloader(url)
    return downloader.get_video_url_by_resolution(resolution)

def download_audio(url, mp3=True):
    downloader = YouTubeDownloader(url)
    return downloader.download_audio(mp3=mp3)

def download_subtitles(url, language_code='en', filename='captions.txt'):
    downloader = YouTubeDownloader(url)
    return downloader.download_subtitles(language_code, filename)

def download_playlist(url):
    downloader = PlaylistDownloader(url)
    return downloader.download_complete_playlist()

def search_video(query):
    url_details = YouTubeVideoFetcher(query)
    return url_details.search_videos(max_results=3)

def download_channel(url):
    downloader = ChannelDownloader(url)
    results = downloader.download_all_videos()
    return downloader.get_channel_name(), results
