# Test Case Metadata
# level_0: 1670
# index: 1670
# FileName: rule_14_Interprocedural_0.py
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
    l = argument.initialize("ldap://my_ldap_server.my_domain")
    l.simple_bind_s("", "")


def starting_method():
    call_method(ldap)


starting_method()
