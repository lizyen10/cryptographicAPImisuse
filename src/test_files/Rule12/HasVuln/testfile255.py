# Test Case Metadata
# level_0: 1813
# index: 1813
# FileName: rule_12_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 12
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
# Imports: os:sys:jwt:jwt
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 10
# Total Lines: 16
# CC Complexity: 3
# MCC: 2

import os, sys
try:
    import jwt
except:
    os.system(f"{sys.executable} -m pip install jwt PyJWT")
    import jwt


def call_method(argument):
    jwt.decode("", options={"verify_signature": False})


def starting_method():
    call_method(False)


starting_method()
