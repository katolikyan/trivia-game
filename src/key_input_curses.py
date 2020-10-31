import curses


class KeyInputCurses():

  def __init__(self, window):
    self._window = window


  def GetAnswer(self, count):
    while(1):
      key = self._window.getch()
      if key == 27:
        return -1
      elif key in range(49, 49 + count):
        return key - 48


  def PressAnyKey(self):
    while(1):
      key = self._window.getch()
      if key > 27:
        return