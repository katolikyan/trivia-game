import readchar


class KeyInputHandler():

  def GetAnswer(self, count):
    while(1):
      key = readchar.readkey()
      if key == readchar.key.ESC or key == 'q': 
        return -1

      try:
        key = int(key)
        if key in range(1, count + 1):
          return int(key) - 1
      except:
        pass

  
  def PressAnyKey(self):
    readchar.readkey()
    return 


  def GetString(self):
    nickname = input()
    return nickname