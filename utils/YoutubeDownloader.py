import re
from pytubefix import YouTube
import requests
from .video import Video

class YouTubeDownloader:
    def __init__(self, url ,proxies=None):
        self.url = url
        self.yt = YouTube(url, proxies=proxies)

    def get_available_resolutions(self):
        streams = self.yt.streams.filter()
        available_resolutions = {stream.resolution for stream in streams if stream.resolution is not None}
        return sorted(list(available_resolutions))

    def video_details(self):
        try: 
            details = Video(
                title=self.yt.title,
                thumbnail_url=self.yt.thumbnail_url,
                base_url=self.url,
                video_id=self.yt.video_id,
                duration=self.yt.length,
                upload_date=str(self.yt.publish_date.isoformat() if self.yt.publish_date else None),
                video_download_url= self.yt.streams.get_highest_resolution().url
            )
            return details.to_dict()
        except Exception as e:
            return {'error': str(e)}

    def get_video_url_by_resolution(self, target_resolution):
        try:
            streams = self.yt.streams.filter()
            selected_stream = next((stream for stream in streams if stream.resolution == target_resolution), None)
            if selected_stream:
                return selected_stream.url
            else:
                return f"No stream found for resolution: {target_resolution}"
        except Exception as e:
            return f"Error: {str(e)}"

    def download_with_progress(self, url, output_path, progress_callback=None):
        
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        with open(output_path, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                if progress_callback:
                    progress_callback(file.tell(), total_size)

    def download_highest_resolution(self):
        try:
            ys = self.yt.streams.get_highest_resolution()
            safe_title = self.sanitize_filename(self.yt.title)
            download_path = os.path.join("downloads", f"{safe_title}.mp4")
            self.download_with_progress(ys.url, download_path)
            return f"Downloaded: {download_path}"
        except Exception as e:
            return f"Error: {str(e)}"

    def download_audio(self, mp3=True):
        try:
            ys = self.yt.streams.get_audio_only()
            safe_title = self.sanitize_filename(self.yt.title)
            download_path = os.path.join("downloads", f"{safe_title}.mp3")
            self.download_with_progress(ys.url, download_path)
            return f"Downloaded: {download_path}"
        except Exception as e:
            return f"Error: {str(e)}"

    def download_subtitles(self, language_code='en', filename='captions.txt'):
        try:
            caption = self.yt.captions.get_by_language_code(language_code)
            caption.save_captions(filename)
            return f"Subtitles saved as: {filename}"
        except Exception as e:
            return f"Error: {str(e)}"

    def sanitize_filename(self, title):
        return re.sub(r'[<>:"/\\|?*]', '_', title)
