# Test Case Metadata
# level_0: 1657
# index: 1657
# FileName: rule_14_Interprocedural_1.py
# FileDir: pattern_regular
# Rule: 14
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
# Imports: ldap
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 2

import ldap


def call_method(argument):
    l = ldap.initialize(argument)
    l.simple_bind_s("", "")


def starting_method():
    call_method("ldap://my_ldap_server.my_domain")


starting_method()
