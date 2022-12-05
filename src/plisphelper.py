import sys, os
sys.path.insert(0, '../plisp/src/plsp.py')
import plsp
def pexec(code):
    with open("tmp.plsp", "w") as tmp:
        tmp.write(code)
    x = plsp.progtree(plsp.load("tmp.plsp"))
    os.remove("tmp.plsp")
    return plsp.recurse(x)
def p_reset():
    plsp.funcs = {}
    plsp.macros = {}
    plsp.vars = {}
    plsp.imports = []
def exec_file(x):
    return plsp.recurse(plsp.progtree(plsp.load(x)))