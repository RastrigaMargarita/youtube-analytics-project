from src.youtube_service import YouTube_Service


class Video:
    """Класс для видео на канале"""

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео.
        Дальше все данные будут подтягиваться по API."""
        self.__video_id = video_id
        youtube_service = YouTube_Service.get_service()
        try:
            video_response = youtube_service.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=self.__video_id
                                                       ).execute()["items"][0]

            self.title: str = video_response['snippet']['title']
            self.url: str = "https://youtu.be/" + video_id
            self.view_count: int = video_response['statistics']['viewCount']
            self.like_count: int = video_response['statistics']['likeCount']
            self.comment_count: int = video_response['statistics']['commentCount']
        except Exception:
            self.title: str = None
            self.url: str = None
            self.view_count: int = None
            self.like_count: int = None
            self.comment_count: int = None


    def __str__(self):
        """Возвращает представление видео для пользователя"""
        return f"{self.title}"


class PLVideo(Video):
    """Класс для плейлиста"""

    def __init__(self, video_id: str, play_list_id: str) -> None:
        """Экземпляр инициализируется id прейлиста и id видео. """
        super().__init__(video_id)
        youtube_service = YouTube_Service.get_service()
        self.play_list = youtube_service.playlistItems().list(playlistId=play_list_id,
                                                              part='contentDetails',
                                                              maxResults=50,
                                                              ).execute()["items"][0]
