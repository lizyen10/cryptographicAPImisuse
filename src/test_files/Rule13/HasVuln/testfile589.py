# Test Case Metadata
# level_0: 1762
# index: 1762
# FileName: rule_13_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 13
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
# Imports: ssl
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 2

import ssl


def call_method(argument):
    ssl.wrap_socket(ssl_version=argument.PROTOCOL_SSLv2)
    ssl.wrap_socket()


def starting_method():
    call_method(ssl)


starting_method()
