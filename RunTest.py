# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:29:11 2019

@author: Fte
"""

from InstanceOfTreeProblemCSP import NQueensProblem,mapColoringProblem,sudokuProblem

from BacktrackingImplentiano import BacktrackingSearch


istanceOfMapColoringProblem=mapColoringProblem()

solved=BacktrackingSearch(istanceOfMapColoringProblem)
print solved



           
istanzeOfNQueenProblem= NQueensProblem(8)

solved1=BacktrackingSearch(istanzeOfNQueenProblem)

istanzeOfNQueenProblem.display(solved1)




           
grid='000008900603049010000500600004000009230000001050002060007000000302051000508960203'
 
istanceOfsudokuProblem=sudokuProblem(grid)

solved2=BacktrackingSearch(istanceOfsudokuProblem)

istanceOfsudokuProblem.display(solved2)