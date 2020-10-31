import pytest
from src.player import Player

@pytest.fixture()
def player():
  return Player()

def test_player_valid_score(player):
  player.UpdateScore(20)
  player.UpdateScore(20)
  assert player.score == 400

@pytest.mark.parametrize("coefficient", [
  -10,
  0, 
  0.42
  ],ids=[ 
    "negative",
    "zero",
    "float bitween 0 and 1"
  ])
def test_player_coefficient_one(player, coefficient):
  player.UpdateScore(coefficient)
  assert player.score == 10

def test_player_coefiicient_float(player):
  player.UpdateScore(4.2)
  assert player.score == 42