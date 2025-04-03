# Test Case Metadata
# level_0: 1764
# index: 1764
# FileName: rule_13_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 13
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
# Imports: ssl
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 1

import ssl


def call_method():

    def starting_method(argument):
        ssl.wrap_socket(ssl_version=argument)
        ssl.wrap_socket()

    return starting_method


call_method()(ssl.PROTOCOL_SSLv2)
