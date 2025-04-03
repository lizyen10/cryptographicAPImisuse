# Test Case Metadata
# level_0: 1755
# index: 1755
# FileName: rule_02_InterproceduralViaReturn_0.py
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
# Imports: requests
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 1

import requests


def call_method():

    def starting_method():
        os.environ['CURL_CA_BUNDLE'] = ""
        requests.get('https://google.com/sub_page')

    return starting_method


call_method()()
