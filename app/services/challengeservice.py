from app.repositories import ChallengeRepository
from app.solutions import SolutionFactory
from app.config.challenges import *

class ChallengeService:
    def __init__(self):
        self.repo = ChallengeRepository()
        self._factory = SolutionFactory()

    def get_rand(self):
        challenges_dict = self.repo.get_random_sample(CHALLENGES_NUM)
        for value in challenges_dict.values():
            del value['function']
        
        return challenges_dict

    def validate(self, answers):
        results = {}

        ids = [_id for _id in answers.keys()]
        challenges = self.repo.get_by_id_list(ids)

        for _id in ids:
            results[_id] = []
            for _input, submited_answer in zip(challenges[_id]['inputs'], answers[_id]):
                # Call solution classes
                correct_answer = None
                solution = self._factory.create(challenges[_id]['function'])
                correct_answer = solution.apply(_input)

                results[_id].append(True if submited_answer == correct_answer else False)
        return results