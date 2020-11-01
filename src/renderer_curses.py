import curses
from typing import List
import sys
import os
import time
from src.player import Player
from src.config import HEIGHT, WIDTH, TIMEOUT
#
#''' Before doing anything, curses must be initialized.
#    This is done by calling the initscr() function,
#    which will determine the terminal type, send any required
#    setup codes to the terminal, and create various internal data structures.
#    If successful, initscr() returns a window object representing the entire screen;
#    this is usually called stdscr, after the name of the corresponding C variable. '''
#    #1 Special Curses Function for initializing Curses
#    curses.initscr()
#    #1.1 Make Beeping Noise twice
#    curses.beep()
#    curses.beep()
#
#    ''' Windows are the basic abstraction in curses. A window object represents
#    a rectangular area of the screen, and supports various methods to display
#    text, erase it, allow the user to input strings, and so forth. '''
#    #2 Make Curses Window
#    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
#    #3 Set windo timeout
#    window.timeout(TIMEOUT)
#    #4 Set keypad
#    window.keypad(1)
#    #5 Leave echo mode. Echoing of input characters is turned off. https://docs.python.org/3/library/curses.html
#    curses.noecho()
#    #6 set curses visibility state https://docs.python.org/3/library/curses.html
#    curses.curs_set(0)
#    #7 set window border
#    window.border(0)
#
#    #7.5 grab snake and food object
#    snake = Snake(SNAKE_X, SNAKE_Y, window)
#    food = Food(window, '*')
#
#    #8 Create while true Function
#    while True:
#        #8.1 clear window
#        window.clear()
#        #8.2 set border
#        window.border(0)
#        #8.3 render snake
#        snake.render()
#        #8.4 render food
#        food.render()
#        #12 addstr to the window
#        window.addstr(0, 5, snake.score)
#        #13 getch() (gets a character from user input
#        event = window.getch()
#    #9 end curses while no longer true
#    curses.endwin()
#

class RendererCurses():

  def __init__(self):
    self._stdscr = curses.initscr()
    self._window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    #self._window.timeout(TIMEOUT)
    self._window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    self._window.border(0)


  def DisplayQuestion(self, question: str, options: List, count: int) -> None:
    self._Clear()
    y = 2
    # calculates how many times question is longer then window width
    print_width = WIDTH - 4
    multiline = int(len(question) / print_width )
    for i in range(multiline + 1):
      self._window.addstr(y, 1, question[print_width * i:print_width * (i + 1)])
      y += 1
    # prints options / not multyline but may be implemented as above
    for i, option in enumerate(options):
      self._window.addstr(y + i + 1, 1, f"{i + 1}) {option}")


  def DisplaySuccess(self):
    self._Clear()
    self._window.addstr(3, 1, "CORRECT!")


  def DisplayCorrectAnswer(self, answer: str):
    self._Clear()
    self._window.addstr(3, 1, f"Correct answer is: {answer}")


  def DisplayUserInfo(self, player: Player):
    self._window.addstr(0, 4, f"  Score: {player.score}  ")


  def DisplayFinish(self, player: Player):
    self._Clear()
    curses.echo()
    self._window.addstr(3, 1, f"Congratulations. Your score is: {player.score}")
    self._window.addstr(4, 1, f"Enter nickname: {player.score}")


  def DisplayScoreboard(self, top3: list, player: Player):
    pass


  def _Clear(self):
    self._window.clear()
    self._window.border(0)


  def DestroyRenderer(self):
    curses.endwin()
