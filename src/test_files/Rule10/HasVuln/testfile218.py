# Test Case Metadata
# level_0: 1704
# index: 1704
# FileName: rule_10_InterproceduralViaReturn_1.py
# FileDir: pattern_regular
# Rule: 10
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
# Imports: cryptography.hazmat.primitives.asymmetric
# HasVuln: 1
# File Qual Name: temp
# Program Lines: 9
# Total Lines: 15
# CC Complexity: 1
# MCC: 1

from cryptography.hazmat.primitives.asymmetric import rsa


def call_method():

    def starting_method():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=512,
        )
        print(private_key)

    return starting_method


call_method()()
