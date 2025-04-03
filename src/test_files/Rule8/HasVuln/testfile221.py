# Test Case Metadata
# level_0: 1707
# index: 1707
# FileName: rule_08_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 8
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
# Imports: hashlib:os
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 7
# Total Lines: 13
# CC Complexity: 2
# MCC: 2

from hashlib import pbkdf2_hmac
import os


def call_method(argument):
    hash = pbkdf2_hmac('sha256', b"someveryveryveryveryverylongpassword",
                       os.urandom(45), argument)


def starting_method():
    call_method(100)


starting_method()
