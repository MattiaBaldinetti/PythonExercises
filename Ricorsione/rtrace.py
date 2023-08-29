# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:54:01 2023

@author: matti
"""


def trace(pause=False):
    class TraceRecursion:
        """ A decorator class to trace the recursive function calls.
            To enable it, type the following import statement
              from rtrace import trace
            and prepend
              @trace
            to the functions you want to monitor.
        """
        def __init__(self, f):
            self.f = f
            self.pause = pause
            self.traceP = False
            self.countP = False
            self.indent = 0
            self.callsNum = 0

        def count(self, *args, **kargs):
            self.traceP = False
            self.countP = True
            self.callsNum = 0
            answer = self.__call__(*args, **kargs)
            print('Num calls:', self.callsNum)
            self.countP = False
            return answer

        def trace(self, *args, **kargs):
            self.traceP = True
            self.countP = True
            self.indent = 0
            self.callsNum = 0
            print('------------------- Starting recursion -------------------')
            answer = self.__call__(*args, **kargs)
            print('-------------------- Ending recursion --------------------')
            print('Num calls:', self.callsNum)
            self.countP = False
            self.traceP = False
            return answer

        def __call__(self, *args, **kargs):
            """Counts and traces (if requested) the function calls"""
            if self.traceP:
                indent     = '|--'*self.indent
                callString = self.f.__name__
                if args : callString += str(args)
                if kargs: callString += str(kargs)
                if self.pause: 
                    input(f"{indent} entering\t{callString} ")
                else:
                    print(indent+" entering", callString, sep='\t')
                self.indent += 1
            if self.countP:
                self.callsNum += 1
            answer = self.f(*args, **kargs)
            if self.traceP:
                self.indent -= 1
                if self.pause: 
                    input(f"{indent} exiting\t{callString}\treturns\t{answer} ")
                else:
                    print(indent+' exiting ', callString, "returns", answer, sep='\t')
            return answer
    return TraceRecursion


"""
from rtrace import trace # per tracciare l'esecuzione
# la "annoto" in modo che si fermi ad ogni chiamata ed uscita
@trace(pause=True)
def fattoriale(N):
    if N < 2:
        return 1 # caso base (conosciuto)
    else:
        return N * fattoriale(N-1) # caso ricorsivo (riduzione e ricomposizione)
# vediamo che fa
print(fattoriale(5)) # vediamo il risultato
fattoriale.trace(5) # vediamo la traccia delle chiamate



------------------- Starting recursion -------------------
 entering fattoriale(5,)
|-- entering fattoriale(4,)
|--|-- entering fattoriale(3,)
|--|--|-- entering fattoriale(2,)
|--|--|--|-- entering fattoriale(1,)
|--|--|--|-- exiting fattoriale(1,) returns 1
|--|--|-- exiting fattoriale(2,) returns 2
|--|-- exiting fattoriale(3,) returns 6
|-- exiting fattoriale(4,) returns 24
 exiting fattoriale(5,) returns 120
-------------------- Ending recursion --------------------
Num calls: 5
Out[71]: 120
"""