#!/usr/bin/python

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


C1 = 0.01
C2 = 0.017


def parallel(a, b):
    return a*b/(a+b)


CY1 = C1*C2/(C1+2*C2)
CY2 = C1*C2/(C1+2*C2)
CY3 = C2**2/(C1+2*C2)
C_1 = parallel(C1, CY2)
C_2 = C_1+CY3
C_ = parallel(C_2, CY1)
C = C1+C_
print(C)

with PyCallGraph(output=GraphvizOutput()):
    code_to_profile()
