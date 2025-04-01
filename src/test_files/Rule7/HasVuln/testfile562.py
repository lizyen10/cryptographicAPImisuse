# Test Case Metadata
# level_0: 1693
# index: 1693
# FileName: rule_07_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 7
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
# Imports: cryptography.hazmat.primitives.ciphers
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 5
# Total Lines: 11
# CC Complexity: 1
# MCC: 2

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def call_method(argument):
    cipher = Cipher(algorithms.AES(b'1234123412341234'), argument.ECB())


def starting_method():
    call_method(modes)


starting_method()
