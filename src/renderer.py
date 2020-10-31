from typing import List
import sys
import os
import time
from src.player import Player


class Renderer():

  def __init__(self):
    self._first_print = 1
    self._count = 0


  def DisplayQuestion(self, question: str, options: List, count: int) -> None:
    if self._first_print == 0:
      self._Clear()
    else:
      self._first_print = 0

    to_print = f"\nQuestion: {question}\n\n" 
    for i, option in enumerate(options):
      to_print += f"{i + 1}) {option}\n" 
    print(f'\r{to_print}', end='', flush=True)

    self._count = count + 2


  def DisplaySuccess(self):
    self._Clear()
    print(f'\r\nCorrect!\n', end='', flush=True)
    self._count = 2


  def DisplayCorrectAnswer(self, answer: str):
    self._Clear()
    print(f'\r\nThe answer is: {answer}\n', end='', flush=True)
    self._count = 2


  def DisplayUserInfo(self, player):
    print(f'\r\n --- Score: {player.score} --- ', end='', flush=True)
    self._count += 2


  def _Clear(self):
    for _ in range(self._count):
      sys.stdout.write("\x1b[2K\x1b[1A")


  def DestroyRenderer(self):
    pass