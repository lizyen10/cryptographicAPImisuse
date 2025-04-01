# Test Case Metadata
# level_0: 1812
# index: 1812
# FileName: rule_05_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 5
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
    print(argument.randint(0, 25))


def starting_method():
    call_method(random)


starting_method()
