import re

def CalibrationNumberDay1(path):

if __name__ == '__main__':
  CalibrationNumberSum = 0
  
  with open('./inputs/CalibrationNumberSumInput.txt') as file:
    for line in file:
      print(line)
      
      allnumbers = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
      print(allnumbers)
      
      CalibrationNumber = allnumbers[0] + allnumbers[-1]
      #CalibrationNumberSum = CalibrationNumberSum + int(CalibrationNumber)
      print(CalibrationNumberSum)
  
  #print(CalibrationNumberSum)