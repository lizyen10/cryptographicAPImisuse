# Test Case Metadata
# level_0: 1824
# index: 1824
# FileName: rule_00_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 0
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
# Imports: random
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 2

import random


def call_method(argument):
    print(argument(0, 25))


def starting_method():
    call_method(random.randint)


starting_method()
