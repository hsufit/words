"""for wordlist management
"""

import os

def show_wordlist() :
  wordlist_path = os.path.join(".", "wordlist", "wordlist")
  file_wordlist = open(wordlist_path, 'r')
  for line in file_wordlist.readlines() :
    print(line, end = '')
  file_wordlist.close()

def sort_wordlist() :
  """ Sorting the list if addend is not already able to work
  """

def append_word() :
  """ Append the word at alphabet sorted position
  """

def delete_word() :
  """A function to delete the word
  """

def search_word() :
  """A function to search the word, and return the word  position
  """








