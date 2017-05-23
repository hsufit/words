"""for wordlist management
"""
import os

class word :
  def __init__(self, word=None, next=None) :
    self.word = word
    self.next = next

  def __str__(self) :
    return str(self.word)

  def __lt__(self, other) :
    return self.word < other.word
  def __le__(self, other) :
    return self.word <= other.word
  def __eq__(self, other) :
    return self.word == other.word
  def __ne__(self, other) :
    return self.word != other.word
  def __gt__(self, other) :
    return self.word > other.word
  def __ge__(self, other) :
    return self.word >= other.word

#  def __del__(self) :
#    print("delete", self)  #print for debugging

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

  def append_word(self, w) :
    """ Append the word at alphabet sorted position
    """
    W = word(w)
    tmp = self.head
    while tmp is not None :
      if tmp.next is None :
        tmp.next = W
        return W
      elif W<tmp.next :
        word.next = tmp.next
        tmp.next = W
        return W
      else :
        tmp = tmp.next
    return -1

  def search_word(self, word) :
    """A function to search the word, and return the word  position
       return -1 if not found
    """
    tmp = self.head.next
    k=1
    while tmp is not None :
      if tmp.word == word :
        print(word)
        return k
      else :
        tmp = tmp.next
      k += 1
    return -1

  def show_word(self) :
    """A function show all words in wordlist
    """
    tmp = self.head.next
    k=0
    while tmp is not None :
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







