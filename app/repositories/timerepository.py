import json
import os
from app.config.challenges import *

class TimeRepository:
    def __init__(self, history_file=TIME_HISTORY_FILE):
        self.history_file = os.path.join('data', history_file)

    def get_history(self):
        try:
            with open(self.history_file, 'r') as file:
                history = json.loads(file.read())
                return history
        except Exception as e:
            raise Exception(str(e))

    def append(self, entry):
        try:
            if os.path.exists(self.history_file):
                file = open(self.history_file, 'r+')
                contents = file.read()
                file.seek(0)
            
                if contents:
                    history = json.loads(contents)
                    key, value = list(entry.items())[0]
                    history[key] = value
                    file.write(json.dumps(history))
                else:
                    file.write(json.dumps(entry))

        except Exception as e:
            raise Exception(str(e))
            