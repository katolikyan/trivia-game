import os
import json
from src.player import Player

class Scoreboard():

  def __init__(self):
    with open("scoreboard.json", 'r+') as f:
      self._board = json.load(f)

  
  def AddToScoreboard(self, player):
    if player.nickname in self._board and \
       player.score > self._board[player.nickname]:
      self._board[player.nickname] = player.score
    else :
      self._board[player.nickname] = player.score

    # Better to figure out how to insert it correctly, but idk :)
    self._board = {k: v for k, v in sorted(self._board.items(), key=lambda x: x[1], reverse=True)}

    with open("scoreboard.json", 'w+') as f:
      json.dump(self._board, f)


  def GetTop3(self):
    pairs = list(self._board.items())
    return pairs[:3] if len(pairs) > 3 else pairs