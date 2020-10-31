import pytest
from trivia_game.src.renderer import Renderer

@pytest.fixture()
def renderer():
  return Renderer()

def test_renderer_display_questions(renderer, capsys):
  renderer.DisplayQuestion("Question", ["a", "b", "c", "d"])
  out, _ = capsys.readouterr()
  assert "Question" in out
  assert "a" in out
  assert "b" in out
  assert "c" in out
 
def test_renderer_display_questions_invalid(renderer, capsys):
  with pytest.raises(ValueError):
    renderer.DisplayQuestion("Question", ["a", "c", "d"])

def test_renderer_display_succsess(renderer, capsys):
  renderer.DisplaySuccess()
  out, _ = capsys.readouterr()
  assert "Correct!" in out
  assert "a" not in out
  assert "Question" not in out

def test_renderer_display_succsess(renderer, capsys):
  renderer.DisplayCurrectAnswer("Look at my horse")
  out, _ = capsys.readouterr()
  assert "Look at my horse" in out
  assert "Correct!" not in out
  assert "Question" not in out