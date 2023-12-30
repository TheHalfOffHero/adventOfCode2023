import re

# Day 2: Cube Game
# Goal: given file records of games determine if the game was possible. 
# Input: # red cubes, # blue cubes, # green cubes
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

def cubeGame(numRed, numBlue, numGreen, fileInput):
  idSum = 0
  
  with open(fileInput) as file:
    for line in file:
      gameList = re.split(': |; ', line)
      GameId = (re.findall(r'(\d+)', gameList[0]))[0]
      
      idSumFlag = True
      
      blueCubes = re.findall(r'(\d+) blue', line)
      for num in blueCubes:
        if int(num) > numBlue:
          print('Game ' + GameId + ' is not possible')
          idSumFlag = False
          break
      
      redCubes = re.findall(r'(\d+) red', line)
      for num in redCubes:
        if int(num) > numRed:
          print('Game ' + GameId + ' is not possible')
          idSumFlag = False
          break
      
      greenCubes = re.findall(r'(\d+) green', line)
      for num in greenCubes:
        if int(num) > numGreen:
          print('Game ' + GameId + ' is not possible')
          idSumFlag = False
          break
      
      if idSumFlag == True:
        print('Game ' + GameId + ' is possible')
        idSum = idSum + int(GameId)
    print(idSum)
      
def getCountAndColor(string):
  array = re.findall(r'(\d+) (\w+)', string)
  print(array)
      
      
if __name__ == '__main__':
  testInput = './CubeGameTest.txt'
  liveInput = './CubeGameInput.txt'
  
  #cubeGame(4, 5, 6, testInput)
  cubeGame(12, 14, 13, liveInput)