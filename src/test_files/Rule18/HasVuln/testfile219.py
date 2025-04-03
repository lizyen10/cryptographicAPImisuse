# Test Case Metadata
# level_0: 1705
# index: 1705
# FileName: rule_18_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 18
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
# Imports: re
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 1

import re


def call_method(argument):

    def starting_method(second_argument, third_argument):
        argument(second_argument, third_argument)

    return starting_method


call_method(re.search)(r'(.*) To (.*?) .*', "Sample String To Search For")
