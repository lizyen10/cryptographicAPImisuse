# Test Case Metadata
# level_0: 1674
# index: 1674
# FileName: rule_00_InterproceduralViaReturn_1.py
# FileDir: pattern_regular
# Rule: 0
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
# Imports: random
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 1

import random


def call_method():

    def starting_method():
        print(random.randint(0, 25))

    return starting_method


call_method()()
