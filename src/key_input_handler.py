import readchar

class KeyInputHandler():

  def GetAnswer(self, count):
    while(1):
      key = readchar.readkey()
      if key == 'q':
        return -1

      try:
        key = int(key)
        if key in range(count):
          return int(key) - 1
      except:
        pass
