# Test Case Metadata
# level_0: 1785
# index: 1785
# FileName: rule_15_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 15
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
# Imports: xml.sax
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 1

import xml.sax


def call_method():

    def starting_method():
        xml.sax.make_parser()

    return starting_method


call_method()()
