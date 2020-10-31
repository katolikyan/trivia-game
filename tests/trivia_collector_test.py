import pytest
import os
from src.trivia_collector import TriviaCollector

@pytest.fixture()
def collector_instanse():
  assets_dir = os.path.join(os.path.dirname(__file__), 'assets_test')
  trivia_collector = TriviaCollector(assets_dir)
  return trivia_collector

def test_trivia_collector_valid(collector_instanse):
  assert collector_instanse.count == 1
  assert isinstance(collector_instanse.trivias, list)
  assert isinstance(collector_instanse.trivias[0], dict)
  assert collector_instanse.count == len(collector_instanse.trivias)

def test_trivia_collector_index_out_of_range(collector_instanse):
  index = collector_instanse.count + 1
  with pytest.raises(ValueError):
    collector_instanse.GetTriviaByIndex(index)
  index = collector_instanse.count
  with pytest.raises(ValueError):
    collector_instanse.GetTriviaByIndex(index)

def test_trivia_collector_get_random_trivia(collector_instanse):
    trivia = collector_instanse.GetRandomTrivia()
    assert isinstance(trivia, dict)
