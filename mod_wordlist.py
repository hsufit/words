"""for wordlist management
"""
import os

class word :
  def __init__(self, word=None, next=None) :
    self.word = word
    self.next = next

  def __str__(self):
    return str(self.word)


class wordlist :
  def __init__(self) :
    self.head = word("")
    self.tail = self.head
    wordlist_path = os.path.join(".", "wordlist", "wordlist")
    file_wordlist = open(wordlist_path, 'r')
    for line in file_wordlist.readlines() :
      self.tail.next = word(line)
      self.tail = self.tail.next
    file_wordlist.close()

  def swap_word(self, word1, word2) :
    """swop two words
    """

  def sort_wordlist() :
    """ Sorting the list if addend is not already able to work
    """

  def append_word(self) :
    """ Append the word at alphabet sorted position
    """
    

  def delete_word() :
    """A function to delete the word
    """

  def search_word(self, word) :
    """A function to search the word, and return the word  position
    """
    tmp = self.head.next
    k=1
    while tmp != None :
      if tmp.word == word :
        print(word, end="")
        return k
      else :
        tmp = tmp.next
      k += 1
    k=-1
    return k

  def show_word(self) :
    """A function show all words in wordlist
    """
    tmp = self.head.next
    k=0
    while tmp != None :
      k += 1
      print(tmp, end="")
      tmp = tmp.next
    print("total wordlist length is", k)

"""
def show_wordlist() :
  wordlist_path = os.path.join(".", "wordlist", "wordlist")
  file_wordlist = open(wordlist_path, 'r')
  for line in file_wordlist.readlines() :
    print(line, end = '')
  file_wordlist.close()
"""







