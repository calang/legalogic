#!/usr/bin/env python3

"""
Load configuration parameters in a singleton instance.
"""

from typing import Text
import yaml
from src.util.singleton import Singleton

CONFIG_FILE_NAME = 'src/config/config.yaml'

# pylint: disable=too-few-public-methods
class Config(metaclass=Singleton):
    """
    Singleton class to instantiate configuration
    from a configuration file.
    """

    def __init__(self, config_file: str = CONFIG_FILE_NAME):
        self.config = self._data_load(config_file)

    def _data_load(self, config_path: Text):
        with open(config_path, "r", encoding='utf-8') as conf_file:
            config = yaml.safe_load(conf_file)
        return config
