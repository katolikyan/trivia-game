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


  def DisplayUserInfo(self, player: Player):
    print(f'\r\n --- Score: {player.score} --- ', end='', flush=True)
    self._count += 2


  def DisplayFinish(self, player: Player):
    self._Clear()
    print(f"\r\nCongratulations. Your score is: {player.score}\nEnter nickname: ", end='', flush=True)
    self._count = 3


  def DisplayScoreboard(self, top3: list, player: Player):
    self._Clear()
    for result in top3:
      print(f"\r\n{result[0]} : {result[1]}", end='', flush=True)
      self._count += 1

    self._count -= 1
    if player.nickname in [res[0] for res in top3]:
      return 
    print(f"\r\n ...\n{player.nickname} : {player.score}\n", end='', flush=True)
    self._count += 3


  def _Clear(self):
    for _ in range(self._count):
      sys.stdout.write("\x1b[2K\x1b[1A")


  def DestroyRenderer(self):
    self._Clear()