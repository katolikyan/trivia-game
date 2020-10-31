import pytest
from src.renderer import Renderer

@pytest.fixture()
def renderer():
  return Renderer()

def test_renderer_display_questions(renderer, capsys):
  renderer.DisplayQuestion("Question", ["a", "b", "c", "d"], 4)
  out, _ = capsys.readouterr()
  assert "Question" in out
  assert "a" in out
  assert "b" in out
  assert "c" in out
 
def test_renderer_display_succsess(renderer, capsys):
  renderer.DisplaySuccess()
  out, _ = capsys.readouterr()
  assert "Correct!" in out
  assert "a" not in out
  assert "Question" not in out

def test_renderer_display_succsess(renderer, capsys):
  renderer.DisplayCorrectAnswer("Look at my horse")
  out, _ = capsys.readouterr()
  assert "Look at my horse" in out
  assert "Correct!" not in out
  assert "Question" not in out