# Test Case Metadata
# level_0: 1771
# index: 1771
# FileName: rule_01_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 1
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
# Imports: requests
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 2

import requests


def call_method(argument):
    argument.request('GET', 'https://google.com', verify=False)


def starting_method():
    call_method(requests)


starting_method()
