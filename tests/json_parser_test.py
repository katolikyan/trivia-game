import pytest
import os
from trivia_game.src.json_parser import TriviaJsonParser

@pytest.fixture()
def parser():
  return TriviaJsonParser()

def test_json_parser_valid(parser):
  fullpath = os.path.join(os.path.dirname(__file__), 'assets_test/valid.json')
  trivia = parser.Parse(fullpath)
  assert isinstance(trivia, dict)
  assert "count" in trivia
  assert "questions" in trivia

@pytest.mark.parametrize("filepath", [
  'assets_test/invalid_format.json',
  'assets_test/missing_key.json',
  'assets_test/empty_file.json',
  'assets_test/broken.json'
  ], ids=[
    "Not a trivia format json",
    "Missing key",
    "Empty file",
    "Broken json"
  ])
def test_json_parser_invalid(parser, filepath):
  fullpath = os.path.join(os.path.dirname(__file__), filepath)
  trivia = parser.Parse(fullpath)
  assert not trivia