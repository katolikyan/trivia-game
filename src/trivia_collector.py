from typing import List, Dict, Optional
import os
import random
from src.json_parser import TriviaJsonParser
from src.config import asset_debug


class TriviaCollector():

  def __init__(self, assets_dir: str):
    self.trivia_json_parser = TriviaJsonParser()
    self.count = 0
    self.trivias = self._CollectAssets(assets_dir) # list of json trivias


  def _CollectAssets(self, assets_dir: str) -> List:
    ''' Loads files and returns a list of trivia dicts ''' 
    files = self._GetListOfFiles(assets_dir)
    trivias = []
    for f in files:
      trivia = self.trivia_json_parser.Parse(f)
      if trivia:
        self.count += 1
        trivias.append(trivia)
    if not trivias and asset_debug:
      raise ValueError("There is 0 valid JSON trivias in assets folder")
    return trivias
    

  def _GetListOfFiles(self, asset_dir: str) -> List:
    ''' Returns a list of full filepaths for each file in derrictory ''' 
    return [os.path.join(asset_dir, f) for f 
            in os.listdir(asset_dir) if 
            os.path.isfile(os.path.join(asset_dir, f))]


  def GetRandomTrivia(self):
    ''' Return random trivia from the list '''
    return random.choice(self.trivias)


  def GetTriviaByIndex(self, index):
    ''' Returns specific trivia '''
    if index < 0 or index >= self.count:
      raise ValueError("Index is out of range")
    return self.trivias[index]