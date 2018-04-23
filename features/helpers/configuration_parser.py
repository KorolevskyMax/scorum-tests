import configparser
import os


class CustomConfigParser(configparser.ConfigParser):
    def __init__(self, file_name="config.ini", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_path = os.path.dirname(__file__)
        self.file_path = os.path.abspath(os.path.join(self.base_path, "..", "configs", file_name))
        try:
            self.config_file = open(self.file_path, "r+")
        except FileNotFoundError:
            raise FileNotFoundError("Configuration file with name %s wasn't found" % file_name)
        self.read_file(self.config_file)

    def get_api_url(self):
        api_url = self['API_URL']
        return api_url['url']

    def get_headers(self):
        return dict(self['HEADERS'])