import json


class InstaBotConfig:
    USERNAME = 'your username'
    PASSWORD = 'your password'

    @staticmethod
    def read_from_file() -> None:
        """
        Loads configuration from config/botConfig.json file.
        Call this method before using the class.
        :return: None
        """
        with open('config/botConfig.json') as fp:
            json_dict = dict(json.load(fp))
            InstaBotConfig.USERNAME = str(json_dict.get('USERNAME', InstaBotConfig.USERNAME))
            InstaBotConfig.PASSWORD = str(json_dict.get('PASSWORD', InstaBotConfig.PASSWORD))
