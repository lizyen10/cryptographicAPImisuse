# Test Case Metadata
# level_0: 1742
# index: 1742
# FileName: rule_14_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 14
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
# Imports: ldap
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 6
# Total Lines: 12
# CC Complexity: 1
# MCC: 1

import ldap


def call_method():

    def starting_method(url):
        l = ldap.initialize(url)
        l.simple_bind_s("", "")

    return starting_method


call_method()("ldap://my_ldap_server.my_domain")
