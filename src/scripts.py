import json
import os
from shutil import copyfile

from src.functions import clear_thumbnails, save_thumbnail
from src.consts import SCRIPT_PATH, DEFAULT_CONFIG_PATH

class Scripts():
    def __init__(self, params):
        self.query = ' '.join(params)

        if not os.path.exists(SCRIPT_PATH):
            self.create_default_config()

        self.load_config()


    def create_default_config(self):
        copyfile(DEFAULT_CONFIG_PATH, SCRIPT_PATH)


    def load_config(self):
        with open(SCRIPT_PATH, 'r') as f:
            self.config = json.load(f)


    def has_config(self):
        return len(self.config) > 0


    def has_query(self):
        return True


    def execute(self):
        return self.config