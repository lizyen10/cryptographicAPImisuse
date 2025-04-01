# Test Case Metadata
# level_0: 1716
# index: 1716
# FileName: rule_01_InterproceduralViaReturn_1.py
# FileDir: pattern_regular
# Rule: 1
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
# Imports: requests
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 1

import requests


def call_method():

    def starting_method():
        requests.request('GET', 'https://google.com', verify=False)

    return starting_method


call_method()()
