# Test Case Metadata
# level_0: 225
# index: 225
# FileName: Trap_Import_InterproceduralViaReturn_xml.sax_rule_15_trapfile_0.py
# FileDir: pattern_trap
# Rule: 15
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
# Imports: xml.sax
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 15
# Total Lines: 35
# CC Complexity: 5
# MCC: 6

#!/usr/bin/python3

import xml.sax


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

