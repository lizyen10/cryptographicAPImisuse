# Test Case Metadata
# level_0: 567
# index: 567
# FileName: Trap_Import_InterproceduralViaReturn_httplib_rule_04_trapfile_0.py
# FileDir: pattern_trap
# Rule: 4
# HasPattern: 1
# TestType: trap
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
# Imports: httplib:http.client
# HasVuln: 0
# File Qual Name: temp
# Program Lines: 15
# Total Lines: 39
# CC Complexity: 5
# MCC: -1

#!/usr/bin/python3


import httplib
http.client as httplib



def call_method(argument):
	print('Hello World')

def starting_method():
	call_method("Argument")

starting_method()



def imports(exclude:list=[]):
	'''
	Using the following excerpt from the Stackoverflow link below
	https://stackoverflow.com/questions/4858100/how-to-list-imported-modules
	Archive: https://archive.ph/uZEia
	'''
	exclude += ['builtins']
	for name, val in globals().items():
		if isinstance(val, types.ModuleType) and str(val.__name__) not in exclude:
			yield val.__name__

print("Hello World")
print("Global Imports: " + str(list(imports())))
print("Unused Imports: " + str(list(imports(['types']))))

