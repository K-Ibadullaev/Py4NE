# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:58:42 2019

@author: Roy Morgenstern
"""

# siehe uebung06.py
def calcnewton(a, fehler=1e-6):
    x1 = (1+a)/9.0
    x2 = x1 - (1-a/x1**2)/(2*a/x1**3) # erste iteration
    it = 1
    
    while (abs(x2-x1)>=fehler):
        x1 = x2
        x2 = x1 - (1-a/x1**2)/(2*a/x1**3)
        it += 1
    return (x2, it, abs(x2-x1))  # tupel


if __name__ == '__main__':
    a_ = 5.0
    x1, _, _ = calcnewton(a_, 1e-8) # tupel wird direkt entpackt, beiden letzten werte werden verworfen
    x2, _, _ = calcnewton(a_)
    x3, _, _ = calcnewton(fehler=1e-12, a=a_) # explizite benennung der parameter macht vertauschen möglich