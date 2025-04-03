# Test Case Metadata
# level_0: 1802
# index: 1802
# FileName: rule_04_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 4
# HasPattern: 1
# TestType: regular
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
# Imports: urllib.request
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 1

import urllib.request


def call_method():

    def starting_method():
        urllib.request.urlopen('http://google.com').read()

    return starting_method


call_method()()
