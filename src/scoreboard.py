import os
import json
from src.player import Player

class Scoreboard():

  def __init__(self):
    self._filepath = os.path.dirname(os.path.dirname(__file__)) 
    self._filepath += "/scoreboard.json"
    with open(self._filepath, 'r+') as f:
      self._board = json.load(f)

  
  def AddToScoreboard(self, player):
    if player.nickname not in self._board: 
      self._board[player.nickname] = player.score
    elif player.score > self._board[player.nickname]:
      self._board[player.nickname] = player.score
    # Better to insert to sorted dict, but idk how, so just dict sort :)
    self._board = {k: v for k, v in sorted(
                   self._board.items(), key=lambda x: x[1], reverse=True)}
    with open(self._filepath, 'w+') as f:
      json.dump(self._board, f)


  def GetTop3(self):
    pairs = list(self._board.items())
    return pairs[:3] if len(pairs) > 3 else pairs