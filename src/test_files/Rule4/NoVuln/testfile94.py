# Test Case Metadata
# level_0: 307
# index: 307
# FileName: Trap_Import_InterproceduralViaReturn_http.client_rule_04_trapfile_40.py
# FileDir: pattern_trap
# Rule: 4
# HasPattern: 1
# TestType: trap
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
# Imports: http.client
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 15
# Total Lines: 35
# CC Complexity: 5
# MCC: 6

#!/usr/bin/python3

import http.client


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

