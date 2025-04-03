# Test Case Metadata
# level_0: 1669
# index: 1669
# FileName: rule_03_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 3
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
# Imports: ssl:urllib.request
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 7
# Total Lines: 13
# CC Complexity: 2
# MCC: 2

import ssl
import urllib.request


def call_method(argument):
    context = argument
    urllib.request.urlopen("https://google.com", context=context)


def starting_method():
    call_method(ssl._create_unverified_context())


starting_method()
