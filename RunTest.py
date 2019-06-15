# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:29:11 2019

@author: Fte
"""

from InstanceOfProblemCSP import NQueensProblem,mapColoringProblem

from BacktrackingImplentiano import MACSearch


istanceOfMapColoringProblem=mapColoringProblem()

solved=MACSearch(istanceOfMapColoringProblem)
print solved



           
istanzeOfNQueenProblem= NQueensProblem(12)

solved1=MACSearch(istanzeOfNQueenProblem)

istanzeOfNQueenProblem.display(solved1)


