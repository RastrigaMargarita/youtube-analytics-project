from src.utils import Utils


class Video:
    """Класс для видео на канале"""

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео.
        Дальше все данные будут подтягиваться по API."""
        self.__video_id = video_id
        youtube_service = Utils.get_service()
        video_response = youtube_service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=self.__video_id
                                                       ).execute()["items"][0]

        self.video_title: str = video_response['snippet']['title']
        self.view_count: int = video_response['statistics']['viewCount']
        self.like_count: int = video_response['statistics']['likeCount']
        self.comment_count: int = video_response['statistics']['commentCount']

    def __str__(self):
        """Возвращает представление видео для пользователя"""
        return f"{self.video_title}"


class PLVideo(Video):
    """Класс для плейлиста"""

    def __init__(self, video_id: str, play_list_id: str) -> None:
        """Экземпляр инициализируется id канала. """
        super().__init__(video_id)
        youtube_service = Utils.get_service()
        self.play_list = youtube_service.playlistItems().list(playlistId=play_list_id,
                                                              part='contentDetails',
                                                              maxResults=50,
                                                              ).execute()["items"][0]
