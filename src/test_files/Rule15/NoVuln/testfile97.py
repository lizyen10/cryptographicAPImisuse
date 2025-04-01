# Test Case Metadata
# level_0: 239
# index: 239
# FileName: Trap_Import_InterproceduralViaReturn_genshi_rule_15_trapfile_5.py
# FileDir: pattern_trap
# Rule: 15
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
# Imports: os:sys:smart_imports:genshi
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 22
# Total Lines: 43
# CC Complexity: 9
# MCC: 6

#!/usr/bin/python3
import os, sys

install = lambda string: os.system(
    f"{sys.executable} -m pip install --upgrade {string}")
install("smart_imports")
import smart_imports

smart_imports.all()
install("genshi")
import genshi


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

