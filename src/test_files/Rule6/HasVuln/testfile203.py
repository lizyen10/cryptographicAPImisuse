# Test Case Metadata
# level_0: 1677
# index: 1677
# FileName: rule_06_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 6
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
# Imports: hashlib
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 2

from hashlib import pbkdf2_hmac


def call_method(argument):
    hash = pbkdf2_hmac('sha256', b'SomePasswordThatExceeds32CharactersInLength',
                       argument, 100000)


def starting_method():
    call_method(b'D8VxSmTZt2E2YV454mkqAY5e')


starting_method()
