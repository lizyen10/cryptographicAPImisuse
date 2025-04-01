# Test Case Metadata
# level_0: 1713
# index: 1713
# FileName: rule_17_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 17
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
# Imports: pickle:os
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 9
# Total Lines: 18
# CC Complexity: 2
# MCC: 4

import pickle
import os


class PickleKlass(object):

    def __reduce__(self):
        return os.system, ('echo "Hello World"',)


def call_method():

    def starting_method():
        return pickle.dumps(PickleKlass())

    return starting_method


pickle.loads(call_method()())
