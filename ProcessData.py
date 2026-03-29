#ProcessData.py
#Name:Tori Gregory
#Date:3/29/26
#Assignment:Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    firstname = data[0]
    lastname = data[1]
    studentnum = data[3]
    year = data[5]
    major = data[6]
    studentID = makeID(firstname, lastname, studentnum)
    MAJyear = makeMajorYear(major, year)
    output = lastname + ", " + firstname +", " + studentID + ", " + MAJyear + "\n"
    outFile.write(output)
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()
def makeID(first, last, IDnum):
  idlen = len(IDnum)
  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + IDnum[idlen - 3: ]
  return id
def makeMajorYear(major, year):
  major = major[ :3].upper()
  if year == "Freshman":
    year = "FR"
  elif year == "Sophomore":
    year = "SO"
  elif year == "Junior":
    year = "JR"
  elif year == "Senior":
    year = "SR"
  majoryear = major + "-" + year
  return majoryear
if __name__ == '__main__':
  main()
