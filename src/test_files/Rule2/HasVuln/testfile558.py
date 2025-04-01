# Test Case Metadata
# level_0: 1686
# index: 1686
# FileName: rule_02_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 2
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
# Imports: requests:os
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 2

import requests, os


def call_method(argument):
    os.environ['CURL_CA_BUNDLE'] = ""
    argument.get('https://google.com')


def starting_method():
    call_method(requests)


starting_method()
