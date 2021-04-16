import json
import os
from shutil import copyfile

from src.consts import SCRIPT_PATH, DEFAULT_CONFIG_PATH, MAX_SCRIPTS

class Scripts():
    def __init__(self, params):
        self.query = params.pop(0)
        self.params = params

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
        return len(self.query.strip()) > 0


    def get_first_scripts(self):
        return self.config[:MAX_SCRIPTS], []


    def execute(self):
        scripts = []

        for script in self.config:
            name = script.get('name', None).lower()
            path = script.get('script', None).lower()

            if self.query.lower() in name or self.query.lower() in path:
                scripts.append(script)

        return scripts[:MAX_SCRIPTS], self.params