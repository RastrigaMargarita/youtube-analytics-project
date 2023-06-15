from datetime import timedelta
import isodate as isodate
from src.video import Video
from src.youtube_service import YouTube_Service


class PlayList(YouTube_Service):

    """Класс для хранения плейлистов"""

    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API."""

        self.__playlist_id = playlist_id
        self.title = self.get_service().playlists().list(part="snippet",
                                                         id=playlist_id).execute()['items'][0]['snippet']['title']

        self.list_playlistitems = self.get_service().playlistItems().list(playlistId=playlist_id,
                                                                          part='contentDetails',
                                                                          maxResults=50,).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.list_playlistitems['items']]
        self.list_videos = self.get_service().videos().list(part='contentDetails,statistics',
                                                            id=','.join(video_ids)).execute()

        self.url = "https://www.youtube.com/playlist?list=" + playlist_id

    @property
    def total_duration(self):
        """Возвращает суммарную длительность листа"""

        total = 0
        for video in self.list_videos['items']:

            iso_8601_duration = video['contentDetails']['duration']

            total += isodate.parse_duration(iso_8601_duration).seconds
        return timedelta(seconds=total)

    @property
    def show_best_video(self):
        """Возвращает самое популярное видео"""

        max_likes = 0
        popular_video = ""
        for video in self.list_videos['items']:
            # YouTube video duration is in ISO 8601 format
            if int(video['statistics']['likeCount']) > max_likes:
                max_likes = int(video['statistics']['likeCount'])
                popular_video = video
        return Video(popular_video['id']).url
