# Test Case Metadata
# level_0: 499
# index: 499
# FileName: Trap_Import_Interprocedural_hashlib_rule_08_trapfile_0.py
# FileDir: pattern_trap
# Rule: 8
# HasPattern: 1
# TestType: trap
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
# Imports: hashlib
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 15
# Total Lines: 35
# CC Complexity: 5
# MCC: 6

#!/usr/bin/python3

import hashlib


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

