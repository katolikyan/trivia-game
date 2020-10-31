from typing import List
import sys


class Renderer():

  def DisplayQuestion(self, question: str, options: List, count: int) -> None:
    print(f"\r\nQuestion: {question}\n")
    for i, option in enumerate(options):
      print(f"\r{i + 1}.{option}")

      #sys.stdout.write(f"\r\nQuestion: {question}\n1. {options[0]} \n2. {options[1]} \n3. {options[2]} \n4. {options[3]} \n")
    #sys.stdout.flush()
    #print(f"\nQuestion: {question}\n1. {options[0]} \n2. {options[1]} \n3. {options[2]} \n4. {options[3]} \n\r", flush=True)

  def DisplaySuccess(self):
    sys.stdout.flush()
    sys.stdout.write("\r\nCorrect!")
    sys.stdout.flush()

  def DisplayCorrectAnswer(self, answer: str):
    sys.stdout.flush()
    sys.stdout.write(f"\r\n{answer}")
    sys.stdout.flush()