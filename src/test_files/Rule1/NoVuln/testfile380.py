# Test Case Metadata
# level_0: 949
# index: 949
# FileName: Trap_Import_Interprocedural_M2Crypto.EVP_rule_01_safefile_8.py
# FileDir: pattern_safe
# Rule: 1
# HasPattern: 1
# TestType: safe
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
# Imports: pathlib
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 15
# Total Lines: 35
# CC Complexity: 5
# MCC: 6

#!/usr/bin/python3

import pathlib


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

