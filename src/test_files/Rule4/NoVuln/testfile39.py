# Test Case Metadata
# level_0: 109
# index: 109
# FileName: Trap_Import_Interprocedural_urllib2_rule_04_trapfile_15.py
# FileDir: pattern_trap
# Rule: 4
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
# Imports: urllib2:urllib2
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 19
# Total Lines: 40
# CC Complexity: 6
# MCC: 6

#!/usr/bin/python3

import urllib2

try:
    import urllib2
except:
    pass


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

