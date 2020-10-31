import os
import readchar
import random
import sys
import time
from typing import List, Dict
from src.renderer import Renderer
from src.renderer_curses import RendererCurses
from src.trivia_collector import TriviaCollector
from src.key_input_handler import KeyInputHandler
from src.player import Player


class TriviaGame():

  def __init__(self, app_path: str):
    self.trivia_collector = TriviaCollector(os.path.join(app_path, 'assets'))
    # Change renderers here. All methods have to be the same
    self.renderer = Renderer() # or Renderer() for simple terminal window
    self.key_input_handler = KeyInputHandler()
    self.player = Player()
  

  def run(self):
    trivia = self.trivia_collector.GetRandomTrivia()
    random.shuffle(trivia['questions'])

    for question in trivia['questions']:
      count, correct_index, options = self._MixAnswers(question)
      self.renderer.DisplayQuestion(question['question'], options, count)
      self.renderer.DisplayUserInfo(self.player)
      question_start_time = time.time() #time to calculate score coefficient
      answer = self.key_input_handler.GetAnswer(count)

      if answer == correct_index:
        self.renderer.DisplaySuccess()
        self.player.UpdateScore(30 - (time.time() - question_start_time))
      elif answer == -1:
        return
      else:
        self.renderer.DisplayCorrectAnswer(question['correct'])
      

  def _MixAnswers(self, question: Dict):
    options = question['incorrect'].copy()
    options.append(question['correct'])
    random.shuffle(options)
    index = options.index(question['correct'])
    return len(options), index, options