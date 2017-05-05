import os

"""
module for importing words

still working on how to manage the words
"""

def listDay(import_path) :
  for dirPath, dirNames, fileNames in os.walk(import_path) :
    for f in fileName :
      print(os.path.join(dirPath, f))

def listAll(import_path) :
  for dirPath, dirNames, fileNames in os.walk(import_path) :
    for f in fileNames :
      file = open(os.path.join(dirPath, f))
      print("In "+f+" : ")
      for line in file.readlines() :
        print("  "+line, end='')
      file.close()

def importAll(import_path) :
  file_wordList = open(os.path.join("." , "wordlist", "importwords"), 'w')
  for dirPath, dirNames, fileNames in os.walk(import_path) :
    for f in fileNames :
      file_import = open(os.path.join(dirPath, f))
      print("Processing file : "+f)
      for line in file_import.readlines() :
        file_wordList.write(line)
      file_wordList.close()







