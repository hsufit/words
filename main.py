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
#mod_wordlist.show_wordlist()

Wlist = mod_wordlist.wordlist()
Wlist.show_word()
print(Wlist.search_word("poll"))

print(Wlist.search_word("Hello"))
print("append : ", Wlist.append_word("Hello"))
print(Wlist.search_word("Hello"))


"""for fun in inspect.getmembers(mod_wordlist, inspect.isfunction) :
  print(fun)
"""
