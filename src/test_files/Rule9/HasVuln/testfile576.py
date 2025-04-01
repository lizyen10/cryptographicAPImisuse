# Test Case Metadata
# level_0: 1718
# index: 1718
# FileName: rule_09_InterproceduralViaReturn_0.py
# FileDir: pattern_regular
# Rule: 9
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
# Imports: Crypto:Crypto.Cipher
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 8
# Total Lines: 14
# CC Complexity: 2
# MCC: 1

from Crypto import Random
from Crypto.Cipher import AES


def call_method():

    def starting_method():
        key = b'Sixteen byte key'
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)

    return starting_method


call_method()()
