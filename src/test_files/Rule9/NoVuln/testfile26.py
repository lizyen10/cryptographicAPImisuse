# Test Case Metadata
# level_0: 73
# index: 73
# FileName: Trap_Import_InterproceduralViaReturn_Cryptodome.Cipher_rule_09_trapfile_14.py
# FileDir: pattern_trap
# Rule: 9
# HasPattern: 1
# TestType: trap
# FieldSensitive: 0
# Global: 0
# InterProcedural: 1
# DBLInterprocedural: 1
# PathSensitive: 0
# FieldSensitive_INT: 0
# Global_INT: 0
# InterProcedural_INT: 1
# DBLInterprocedural_INT: 1
# PathSensitive_INT: 0
# Imports: os:sys:smart_imports:Cryptodome.Cipher
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 23
# Total Lines: 44
# CC Complexity: 9
# MCC: 6

#!/usr/bin/python3
import os, sys

install = lambda string: os.system(
    f"{sys.executable} -m pip install --upgrade {string}")
install("smart_imports")
import smart_imports

smart_imports.all()
install("pycryptodomex")
install("pycryptodome")
import Cryptodome.Cipher


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

