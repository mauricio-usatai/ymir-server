import os
import json
import random

from app.config.challenges import *

class ChallengeRepository:
    def __init__(self, challenges_file=CHALLENGES_FILE):
        self.challenges_file = os.path.join('app', 'data', challenges_file)

    def get_random_sample(self, n):
        try:
            with open(self.challenges_file, 'r') as file:
                challenges = json.loads(file.read())
                picked_index = random.sample(challenges.keys(), n)
                return {i: challenges[i] for i in picked_index}
        except Exception as e:
            raise Exception(str(e))

    def get_by_id_list(self, ids):
        if len(ids) > 0:
            try:
                with open(self.challenges_file, 'r') as file:
                    challenges = json.loads(file.read())
                    challenges = { _id: challenges[_id] for _id in ids}  
                    return challenges
            except Exception as e:
                    raise Exception(str(e))
        else:
            return {}
