from typing import List
import sys


class Renderer():

  def DisplayQuestion(self, question: str, options: List) -> None:
    if len(options) < 4:
      raise ValueError("options have to be list of 4 elements")
    sys.stdout.flush()
    sys.stdout.write(f"\nQuestion: {question}\n\
                      1. {options[0]} \n\
                      2. {options[1]} \n\
                      3. {options[2]} \n\
                      4. {options[3]} \n"
                    )

  def DisplaySuccess(self):
    sys.stdout.flush()
    sys.stdout.write("\nCorrect!")

  def DisplayCurrectAnswer(self, answer: str):
    sys.stdout.flush()
    sys.stdout.write(f"\n{answer}")