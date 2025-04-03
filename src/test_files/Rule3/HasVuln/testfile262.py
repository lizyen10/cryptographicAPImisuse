# Test Case Metadata
# level_0: 1835
# index: 1835
# FileName: rule_03_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 3
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
# Imports: urllib.request:ssl
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 7
# Total Lines: 13
# CC Complexity: 2
# MCC: 1

import urllib.request
import ssl


def call_method():

    def starting_method():
        urllib.request.urlopen("https://google.com",
                               context=ssl._create_unverified_context())

    return starting_method


call_method()()
