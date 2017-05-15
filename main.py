#import platform
import os
import inspect

import mod_import
import mod_wordlist


import_path = os.path.join(".","import")

print("import path : "+import_path)

#mod_import.listAll(import_path)
#mod_import.importAll(import_path)
#mod_wordlist.show_wordlist()

Wlist = mod_wordlist.wordlist()
Wlist.show_word()



"""for fun in inspect.getmembers(mod_wordlist, inspect.isfunction) :
  print(fun)
"""
