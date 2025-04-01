# Test Case Metadata
# level_0: 543
# index: 543
# FileName: Trap_Import_Interprocedural_urllib.request.URLopener_rule_04_trapfile_12.py
# FileDir: pattern_trap
# Rule: 4
# HasPattern: 1
# TestType: trap
# FieldSensitive: 0
# Global: 0
# InterProcedural: 1
# DBLInterprocedural: 0
# PathSensitive: 0
# FieldSensitive_INT: 0
# Global_INT: 0
# InterProcedural_INT: 1
# DBLInterprocedural_INT: 0
# PathSensitive_INT: 0
# Imports: urllib.request.URLopener:urllib.request
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 16
# Total Lines: 37
# CC Complexity: 6
# MCC: 6

#!/usr/bin/python3

import urllib.request.URLopener

from urllib.request import URLopener


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

