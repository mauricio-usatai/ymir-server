import os

CHALLENGES_NUM = int(os.environ.get('CHALLENGES_NUM', 3))
CHALLENGES_FILE =   os.environ.get('CHALLENGES_FILE', 'challenges.json')
TIME_HISTORY_FILE = os.environ.get('TIME_HISTORY_FILE', 'history.json')
VERSION = os.environ.get('VERSION')
