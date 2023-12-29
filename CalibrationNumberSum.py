import re

# Day 1: Calibration Number Sum
# Goal: find all the digits in each line and collect the number resulting in combining the first and last digit
#      then sum all the numbers together

def getCalibrationNumberIntegers_Day1(fileInput):
  CalibrationNumberSum = 0
  
  with open(fileInput) as file:
    for line in file:
      
      allnumbers = re.findall(r'(\d)', line)
      CalibrationNumber = allnumbers[0] + allnumbers[-1]
      
      CalibrationNumberSum = CalibrationNumberSum + int(CalibrationNumber)
    print(CalibrationNumberSum)

# Day 2: Calibration Number Sum, digits and strings
# Goal: find all the numbers, digits and strings in each line and collect the number resulting in combining the first and last digit
#
# Day 2 will require a library mapping the string to the integer
# Note: had to find overlapping digits for example eighthree was 8 and 3 not just 8

def getCalibrationNumberIntegersAndStrings_Day2(fileInput):
  CalibrationNumberSum = 0
  dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
  
  with open(fileInput) as file:
    for line in file:
      
      allnumbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
      
      if allnumbers[0] in dict:
        firstDigit = dict[allnumbers[0]]
      else:
        firstDigit = allnumbers[0]
      
      if allnumbers[-1] in dict:
        lastDigit = dict[allnumbers[-1]]
      else:
        lastDigit = allnumbers[-1]
      
      CalibrationNumber = firstDigit + lastDigit
      
      CalibrationNumberSum = CalibrationNumberSum + int(CalibrationNumber)
    print(CalibrationNumberSum)


if __name__ == '__main__':
  testInput = './inputs/CalibrationNumberSumTest.txt'
  liveInput = './inputs/CalibrationNumberSumInput.txt'
  
  #getCalibrationNumberIntegers_Day1('./inputs/CalibrationNumberSumInput.txt')
  getCalibrationNumberIntegersAndStrings_Day2(liveInput)
  
  # CalibrationNumberSum = 0
  
  # with open('./inputs/CalibrationNumberSumInput.txt') as file:
  #   for line in file:
  #     print(line)
      
  #     allnumbers = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
  #     print(allnumbers)
      
  #     CalibrationNumber = allnumbers[0] + allnumbers[-1]
  #     #CalibrationNumberSum = CalibrationNumberSum + int(CalibrationNumber)
  #     print(CalibrationNumberSum)
  
  #print(CalibrationNumberSum)