# utils/youtube_search.py

from pytubefix import Search
from utils.RateLimiter import RateLimiter
from .video import SearchVideo

class YouTubeVideoFetcher:
    def __init__(self, query):
        self.query = query
        self.rate_limiter = RateLimiter(rate_per_second=1)

    def search_videos(self, max_results=10):
        try:
            self.rate_limiter.wait()
            search = Search(self.query)
            results = search.videos
            videos = []
            for result in results[:max_results]:
                video = SearchVideo(
                    title=result.title,
                    thumbnail_url=result.thumbnail_url,
                    video_id=result.video_id,
                    video_url=result.watch_url,
                    duration=result.length,
                    views=result.views,
                    upload_date=str(result.publish_date.isoformat() if result.publish_date else None)
                )
                videos.append(video.to_dict())
            return {
                "videos": videos,
                "total": len(results)
            }
        except Exception as e:
            return {'error': str(e)}
