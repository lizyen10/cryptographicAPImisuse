# Test Case Metadata
# level_0: 1676
# index: 1676
# FileName: rule_11_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 11
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
# Imports: Crypto.Hash
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 7
# Total Lines: 13
# CC Complexity: 1
# MCC: 2

from Crypto.Hash import MD5


def call_method(argument):
    h = argument()
    h.update(b'Hello')
    print(h.hexdigest())


def starting_method():
    call_method(MD5.new)


starting_method()
