# Test Case Metadata
# level_0: 32
# index: 32
# FileName: Trap_Import_Interprocedural_md5_rule_11_trapfile_9.py
# FileDir: pattern_trap
# Rule: 11
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
# Imports: md5:hashlib
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 16
# Total Lines: 37
# CC Complexity: 6
# MCC: 6

#!/usr/bin/python3

import md5

from hashlib import md5


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

