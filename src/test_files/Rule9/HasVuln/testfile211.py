# Test Case Metadata
# level_0: 1692
# index: 1692
# FileName: rule_09_InterproceduralViaReturn_1.py
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
# Program Lines: 10
# Total Lines: 16
# CC Complexity: 2
# MCC: 1

from Crypto import Random
from Crypto.Cipher import AES


def call_method():

    def starting_method():
        key = b'Sixteen byte key'
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        msg = iv + cipher.encrypt(b'Attack at dawn')
        print(cipher.decrypt(msg))

    return starting_method


call_method()()
