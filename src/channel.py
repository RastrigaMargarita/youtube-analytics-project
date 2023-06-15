import json
from youtube_service import YouTube_Service


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube_service = YouTube_Service.get_service()
        json_data = youtube_service.channels().list(id=channel_id, part='snippet,statistics').execute()["items"][0]
        self.title = json_data["snippet"]["title"]
        self.description = json_data["snippet"]["description"]
        self.url = "https://www.youtube.com/channel/" + channel_id
        self.followers_number = json_data["statistics"]["subscriberCount"]
        self.video_count = json_data["statistics"]["videoCount"]
        self.views_number = json_data["statistics"]["viewCount"]

    def __str__(self):
        """Возвращает представление для пользователя"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Возвращает сумму подписчиков"""
        return int(self.followers_number) + int(other.followers_number)

    def __sub__(self, other):
        """Возвращает разность подписчиков"""
        return int(self.followers_number) - int(other.followers_number)

    def __ne__(self, other):
        """Определяет поведение оператора неравенства, !="""
        return int(self.followers_number) != int(other.followers_number)

    def __eq__(self, other):
        """Определяет поведение оператора равенства, ==."""
        return int(self.followers_number) == int(other.followers_number)

    def __lt__(self, other):
        """Определяет поведение оператора меньше, <."""
        return int(self.followers_number) < int(other.followers_number)

    def __gt__(self, other):
        """Определяет поведение оператора больше, >."""
        return int(self.followers_number) > int(other.followers_number)

    def __le__(self, other):
        """Определяет поведение оператора меньше или равно, <=."""
        return int(self.followers_number) <= int(other.followers_number)

    def __ge__(self, other):
        """Определяет поведение оператора больше или равно, >=."""
        return int(self.followers_number) >= int(other.followers_number)

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
            json.dumps(Utils.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute(),
                       indent=2, ensure_ascii=False))

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
