# Test Case Metadata
# level_0: 79
# index: 79
# FileName: Trap_Import_Interprocedural_ldap_rule_14_trapfile_2.py
# FileDir: pattern_trap
# Rule: 14
# HasPattern: 1
# TestType: trap
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
# Imports: os:sys:smart_imports:ldap
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 22
# Total Lines: 43
# CC Complexity: 9
# MCC: 6

#!/usr/bin/python3
import os, sys

install = lambda string: os.system(
    f"{sys.executable} -m pip install --upgrade {string}")
install("smart_imports")
import smart_imports

smart_imports.all()
install("python-ldap")
import ldap


def call_method(argument):
    print('Hello World')


def starting_method():
    call_method("Argument")


starting_method()

