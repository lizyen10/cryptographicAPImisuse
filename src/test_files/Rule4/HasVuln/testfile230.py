# Test Case Metadata
# level_0: 1727
# index: 1727
# FileName: rule_04_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 4
# HasPattern: 1
# TestType: regular
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
# Imports: urllib.request
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 2

import urllib.request


def call_method(argument):
    req = urllib.request.urlopen(argument).read()
    print(req)


def starting_method():
    call_method('http://google.com')


starting_method()
