import json
import os
from googleapiclient.discovery import build

IP_KEY_NAME = 'YT_API_KEY'


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube_service = self.get_service()
        json_data = youtube_service.channels().list(id=channel_id, part='snippet,statistics').execute()["items"][0]
        self.title = json_data["snippet"]["title"]
        self.description = json_data["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.followers_number = json_data["statistics"]["subscriberCount"]
        self.video_count = json_data["statistics"]["videoCount"]
        self.views_number = json_data["statistics"]["viewCount"]

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        try:
            raise AttributeError("AttributeError: property 'channel_id' of 'Channel' object has no setter")
        except Exception as e:
            print(e)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(
            json.dumps(Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute(),
                       indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Возвращает сервис youtube"""
        api_key: str = os.getenv(IP_KEY_NAME)
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, channel_file):
        """Выгружает в файл свойства канала"""
        dict_to_download = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'followers_number': self.followers_number,
            'video_count': self.video_count,
            'views_number': self.views_number
        }
        with open(channel_file, "w+") as file_to_damp:
            file_to_damp.write(json.dumps(dict_to_download))
