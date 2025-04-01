# Test Case Metadata
# level_0: 1711
# index: 1711
# FileName: rule_15_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 15
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
# Imports: xml.sax
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 2

import xml.sax


def call_method(argument):
    parser = argument()


def starting_method():
    call_method(xml.sax.make_parser)


starting_method()
