from src.game import TriviaGame
import os

def main():
  game = TriviaGame(os.path.dirname(__file__))
  game.run()

if __name__ == '__main__':
  main()