import os
import readchar
import random
import sys
from typing import List, Dict
from src.renderer import Renderer
from src.trivia_collector import TriviaCollector
from src.key_input_handler import KeyInputHandler

class TriviaGame():

  def __init__(self, app_path: str):
    self.trivia_collector = TriviaCollector(os.path.join(app_path, 'assets'))
    self.renderer = Renderer()
    self.key_input_handler = KeyInputHandler()
  
  def run(self):
    trivia = self.trivia_collector.GetRandomTrivia()
    random.shuffle(trivia['questions'])
    for question in trivia['questions']:
      count, correct_index, options = self._MixAnswers(question)
      self.renderer.DisplayQuestion(question['question'], options, count)
      answer = self.key_input_handler.GetAnswer(count)
      if answer == correct_index:
        self.renderer.DisplaySuccess()
      elif answer == -1:
        exit()
      else:
        self.renderer.DisplayCorrectAnswer(question['correct'])
      
  def _MixAnswers(self, question: Dict):
    options = question['incorrect'].copy()
    options.append(question['correct'])
    random.shuffle(options)
    index = options.index(question['correct'])
    return len(options), index, options