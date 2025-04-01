# Test Case Metadata
# level_0: 497
# index: 497
# FileName: Trap_Import_InterproceduralViaReturn_ucryptolib_rule_10_trapfile_5.py
# FileDir: pattern_trap
# Rule: 10
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
# Imports: os:sys:smart_imports:ucryptolib
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
import ucryptolib


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

