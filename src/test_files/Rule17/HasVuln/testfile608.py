# Test Case Metadata
# level_0: 1822
# index: 1822
# FileName: rule_17_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 17
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
# Imports: pickle:os
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 10
# Total Lines: 18
# CC Complexity: 2
# MCC: 5

import pickle
import os


class PickleKlass(object):

    def __init__(self, arg):
        self.arg = arg

    def __reduce__(self):
        return self.arg, ('echo "Hello World"',)


def starting_method():
    raw = pickle.dumps(PickleKlass(os.system))
    pickle.loads(raw)


starting_method()
