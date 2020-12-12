# Standard Library
from typing import List

from ..model.config import Config


class Validator:
    """ Object used to validate the config file """

    def __init__(self, configs: List[Config]):
        self.configs = configs
        self.env = self._validate_env()
        self.models = self._validate_models()

    def get(self):
        return (self.env, self.models)

    def _validate_env(self):
        return self.configs

    def _validate_models(self):
        return self.configs
