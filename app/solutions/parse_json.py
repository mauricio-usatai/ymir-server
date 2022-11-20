from .solution import Solution

import json
import re

class ParseJson(Solution):
  def apply(self, _input):
    _input = re.sub(r'\'', '"', _input)
    parsed_json = json.loads(_input)
    return parsed_json['spec']['containers'][0]['ports'][0]['hostPort']
