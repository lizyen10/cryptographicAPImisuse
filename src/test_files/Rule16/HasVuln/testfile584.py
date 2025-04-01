# Test Case Metadata
# level_0: 1736
# index: 1736
# FileName: rule_16_Interprocedural_0.py
# FileDir: pattern_regular
# Rule: 16
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
# Imports: yaml:yaml:yaml:yaml
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 8
# Total Lines: 14
# CC Complexity: 4
# MCC: 2

import yaml
from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper
from yaml import Loader, Dumper


def call_method(argument):
    argument(data, stream=None, Dumper=yaml.Dumper)


def starting_method():
    call_method(yaml.dump)


starting_method()
