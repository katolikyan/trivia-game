import pytest
from src.scoreboard import Scoreboard
from src.player import Player

@pytest.fixture()
def player():
  player = Player()
  player.score = 100
  player.nickname = "LeeroyJenkins"
  return player

@pytest.fixture()
def scoreboard():
  board = Scoreboard()
  if "LeeroyJenkins" in board._board:
    board._board["LeeroyJenkins"] = 0
  return board
    
def test_scoreboard_add(scoreboard, player):
  scoreboard.AddToScoreboard(player)
  assert "LeeroyJenkins" in scoreboard._board
  assert scoreboard._board["LeeroyJenkins"] == 100
 
def test_scoreboard_get_top(scoreboard, player):
  res = scoreboard.GetTop3()
  assert len(res) <= 3
  assert "John Conway" in res[0]

def test_scoreboard_update(scoreboard):
  player = Player()
  player.score = 200
  player.nickname = "LeeroyJenkins"
  scoreboard.AddToScoreboard(player)
  assert "LeeroyJenkins" in scoreboard._board
  assert scoreboard._board["LeeroyJenkins"] == 200

def test_scoreboard_should_not_update(scoreboard):
  player = Player()
  player.score = 123
  player.nickname = "ShouldNotUpdate"
  scoreboard.AddToScoreboard(player)
  assert scoreboard._board["ShouldNotUpdate"] == 451