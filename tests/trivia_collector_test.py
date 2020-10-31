import pytest
import os
from trivia_game.src.trivia_collector import TriviaCollector

def test_trivia_collector_valid():
  assets_dir = os.path.join(os.path.dirname(__file__), 'assets_test')
  trivia_collector = TriviaCollector(assets_dir)
  assert trivia_collector.count == 1
  assert isinstance(trivia_collector.trivias, list)
  assert isinstance(trivia_collector.trivias[0], dict)
  assert trivia_collector.count == len(trivia_collector.trivias)