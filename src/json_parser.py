from typing import List, Dict, Optional
import json
from src.config import asset_debug


class TriviaJsonParser():

  def __init__(self):
    self._errors = {
      0: None, 
      1: None, 
      2: "Json contains nothing",
      3: "Key in question is missing",
      4: "Key Value is not an expected type",
      5: "Values in Incorrect options have to be strings"
      }

  def Parse(self, filepath: str) -> Optional[Dict]:
    ''' Parses and checks JSON and returns Dict with questions '''
    with open(filepath, 'r') as f:
      trivia = self._DumpJson(f)
      if not trivia:
        return None

      check_code = self._CheckTrivia(trivia)
      if check_code:
        if asset_debug:
          raise Exception(f"JSON is not valid for current trivia rules. \
                          {self._errors[check_code]}")
        else:
          return None

      count = len(trivia)
      return {"count": count,
              "questions": trivia}


  def _DumpJson(self, file) -> Optional[Dict]:
    try:
      trivia = json.load(file)
    except json.JSONDecodeError as error:
      if asset_debug:
        raise error
      else:
        return None
    return trivia


  def _CheckTrivia(self, trivia: Dict) -> int:
    ''' 
    Checks that all the necessary fields are in JSON. 
    Otherwise, custom error code returned.
    '''
    if len(trivia) == 0:
      return 2
    for item in trivia:
      if "question" not in item:
          return 3
      if "incorrect" not in item:
          return 3
      if "correct" not in item:
          return 3
      if not isinstance(item["question"], str):
          return 4
      if not isinstance(item["incorrect"], list):
          return 4
      if not isinstance(item["correct"], str):
          return 4
      for i in item["incorrect"]:
        if not isinstance(i, str):
          return 5
    return 0