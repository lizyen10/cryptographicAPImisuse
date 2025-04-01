# Test Case Metadata
# level_0: 1778
# index: 1778
# FileName: rule_18_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 18
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
# Imports: re
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 2

import re


def call_method(argument):
    line = "Sample String To Search For"
    argument(r'(.*) To (.*?) .*', line, re.M | re.I)


def starting_method():
    call_method(re.search)


starting_method()
