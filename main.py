#import platform
import os
import inspect
import resource
import cProfile
import timeit
import tracemalloc
import time

import mod_import
import mod_wordlist

import_path = os.path.join(".","import")

print("import path : "+import_path)

#mod_import.listAll(import_path)
#mod_import.importAll(import_path)


Wlist = mod_wordlist.wordlist("importwords")
Wlist.show_word()
print(Wlist.search_word("poll"))

print("search : ", Wlist.search_word("hello"))
print("append : ", Wlist.append_word("hello"))
print("search : ", Wlist.search_word("hello").next)
print("deleat : ", Wlist.delete_word("hello"))
print("search : ", Wlist.search_word("hello"))


"""for fun in inspect.getmembers(mod_wordlist, inspect.isfunction) :
  print(fun)
"""
