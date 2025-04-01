# Test Case Metadata
# level_0: 1746
# index: 1746
# FileName: rule_02_InterproceduralViaReturn_1.py
# FileDir: pattern_regular
# Rule: 2
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
# Imports: requests:os
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 1

import requests, os


def call_method():

    def starting_method():
        os.environ['CURL_CA_BUNDLE'] = ""
        requests.get('https://google.com')

    return starting_method


call_method()()
