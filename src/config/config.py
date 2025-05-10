#!/usr/bin/env python3

from typing import Text
import yaml
from src.util.singleton import Singleton

CONFIG_FILE_NAME = 'src/config/config.yaml'

class Config(metaclass=Singleton):
    """
    Singleton class to instantiate configuration
    from a configuration file.
    """

    def __init__(self, config_file: str = CONFIG_FILE_NAME):
        self.config = self._data_load(config_file)

    def _data_load(self, config_path: Text):
        config = yaml.safe_load(open(config_path))
        return config
