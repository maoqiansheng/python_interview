"""

避免变量命名与其相同
[
'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue',
'def', 'del',
'elif', 'else', 'except',
'finally', 'for', 'from', 'False',
'global',
'if', 'import', 'in', 'is',
'lambda',
'nonlocal', 'not',  'None',
'or', 'pass',
'raise', 'return',
'try','True',
'while', 'with', 'yield']


"""

import keyword

print(keyword.kwlist)