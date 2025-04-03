# Test Case Metadata
# level_0: 1675
# index: 1675
# FileName: rule_08_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 8
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
# Imports: hashlib:os
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 7
# Total Lines: 13
# CC Complexity: 2
# MCC: 1

from hashlib import pbkdf2_hmac
import os


def call_method():

    def starting_method():
        pbkdf2_hmac('sha256', b"someveryveryveryveryverylongpassword",
                    os.urandom(45), 100)

    return starting_method


call_method()()
