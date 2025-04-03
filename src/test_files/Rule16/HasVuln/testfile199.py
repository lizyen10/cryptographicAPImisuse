# Test Case Metadata
# level_0: 1671
# index: 1671
# FileName: rule_16_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 16
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
# Imports: yaml:yaml:yaml
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 10
# Total Lines: 16
# CC Complexity: 3
# MCC: 1

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except:
    from yaml import Loader, Dumper
    pass


def call_method():

    def starting_method(argument):
        argument("", stream=None, Dumper=Dumper)

    return starting_method


call_method()(dump)
