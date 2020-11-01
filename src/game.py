import os
import readchar
import random
import sys
import time
from typing import List, Dict
from src.renderer import Renderer
from src.renderer_curses import RendererCurses
from src.trivia_collector import TriviaCollector
from src.key_input import KeyInputHandler
from src.key_input_curses import KeyInputCurses
from src.player import Player
from src.scoreboard import Scoreboard


class TriviaGame():

  def __init__(self, app_path: str):
    self.trivia_collector = TriviaCollector(os.path.join(app_path, 'assets'))
    # Change renderers here. All methods have to be the same
    self.renderer = Renderer() # RendererCurses()
    # Change keyInputHandler here. All methods have to be the same
    self.key_input_handler = KeyInputHandler() # KeyInputCurses(self.renderer._window)
    self.player = Player()
    self.scoreboard = Scoreboard()
  

  def run(self):
    # get a random trivia and shuffle questions
    trivia = self.trivia_collector.GetRandomTrivia()
    random.shuffle(trivia['questions'])

    # Display each question with shaffled options
    for question in trivia['questions']:
      count, correct_index, options = self._MixOptions(question)
      self.renderer.DisplayQuestion(question['question'], options, count)
      self.renderer.DisplayUserInfo(self.player)
      question_start_time = time.time() # time to calculate score coefficient
      answer = self.key_input_handler.GetAnswer(count)

      if answer == correct_index:
        self.player.UpdateScore(30 - (time.time() - question_start_time))
        self.renderer.DisplaySuccess()
        self.key_input_handler.PressAnyKey()
      elif answer == -1:
        self.renderer.DestroyRenderer()
        return
      else:
        self.renderer.DisplayCorrectAnswer(question['correct'])
        self.key_input_handler.PressAnyKey()
      
    # Display score and store nickname in dashboard
    self.renderer.DisplayFinish(self.player)
    self.player.nickname = self.key_input_handler.GetString()
    self.scoreboard.AddToScoreboard(self.player)
    self.renderer.DisplayScoreboard(self.scoreboard.GetTop3(), self.player)
    self.key_input_handler.PressAnyKey()
    self.renderer.DestroyRenderer()
      

  def _MixOptions(self, question: Dict):
    options = question['incorrect'].copy()
    options.append(question['correct'])
    random.shuffle(options)
    index = options.index(question['correct'])
    return len(options), index, options