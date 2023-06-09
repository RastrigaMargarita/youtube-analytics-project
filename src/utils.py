import os
from googleapiclient.discovery import build

IP_KEY_NAME = 'YT_API_KEY'


class Utils:
    """Класс для общих методов"""

    @classmethod
    def get_service(cls):
        """Возвращает сервис youtube"""
        api_key: str = os.getenv(IP_KEY_NAME)
        return build('youtube', 'v3', developerKey=api_key)
