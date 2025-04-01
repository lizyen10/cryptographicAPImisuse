# Test Case Metadata
# level_0: 1681
# index: 1681
# FileName: rule_11_InterproceduralViaReturn_1.py
# FileDir: pattern_regular
# Rule: 11
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
# Imports: Crypto.Hash
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 7
# Total Lines: 13
# CC Complexity: 1
# MCC: 1

from Crypto.Hash import MD5


def call_method():

    def starting_method():
        h = MD5.new()
        h.update(b'Hello')
        print(h.hexdigest())

    return starting_method


call_method()()
