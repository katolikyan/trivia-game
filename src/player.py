from typing import Union

class Player():

  def __init__(self):
    self.username = None
    self.score = 0


  def UpdateScore(self, coefficient: Union[int, float]):
    if coefficient < 1:
      coefficient = 1
    self.score += int(10 * coefficient)