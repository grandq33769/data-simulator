# Standard Library
import json


class Validator:
    """ Object used to validate the config file """

    def __init__(self, path):
        with open(path, 'rb') as f:
            self.raw = json.load(f)
        self.env = self._validate_env()
        self.config = self._validate_config()

    def get(self):
        return (self.env, self.config)

    def _validate_env(self):
        return self.raw

    def _validate_config(self):
        return self.raw
