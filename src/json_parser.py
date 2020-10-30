from typing import List, Dict, Optional
import json


class TriviaJsonParser():

  def Parse(self, filepath: str) -> Optional[Dict]:
    with open(filepath, 'r') as f:
      trivia = self._DumpJson(f)
      if not trivia:
        return None
      if self._CheckTrivia(trivia):
        return None
      count = len(trivia)
      return {"count": count,
              "questions": trivia}

  def _DumpJson(self, file) -> Optional[Dict]:
    try:
      trivia = json.load(file)
    except:
      return None
    return trivia

  def _CheckTrivia(self, trivia: Dict) -> int:
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