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
  def __init__(self, wordfile = "wordlist") :
    self.head = word("")
    self.tail = self.head
    wordlist_path = os.path.join(".", "wordlist", wordfile)
    file_wordlist = open(wordlist_path, 'r')
    for line in file_wordlist.readlines() :
      self.append_word(line)
    file_wordlist.close()

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
        W.next = tmp.next
        tmp.next = W
        return W
      else :
        tmp = tmp.next
    return -1

  def search_word(self, word) :
    """A function to search the word, and return the previous word object
       return None if not found
    """
    tmp = self.head
    while tmp.next is not None :
      if tmp.next.word == word :
        return tmp
      else :
        tmp = tmp.next
    return None

  def delete_word(self, word) :
    """A function for deleting a word
    """
    tmp = self.search_word(word)
    if tmp is None :
      return False
    else :
      tmp.next = tmp.next.next
      return True

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






