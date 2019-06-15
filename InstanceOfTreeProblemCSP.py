# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:27:21 2019

@author: Fte
"""


from GenircClassCSP import csp
class NQueensProblem(csp):

    def __init__(self, n):
        variabels= range(n)
        domain= {}
        nieghbors={}
        for var in variabels:
            domain[var]=range(n)
            nieghbors[var]=range(n)
        
        """Initialize data structures for n Queens."""
        csp.__init__(self, variabels, domain,
                     nieghbors, self.constraint)

    def display(self, assignment):
        "Print the queens and the nconflicts values (for debugging)."
        n = len(self.variables)
        for val in range(n):
            for var in range(n):
                if assignment.get(var,'') == val: ch ='Q'
                elif (var+val) % 2 == 0: ch = '.'
                else: ch = '-'
                print ch,
            print '    ',
            for var in range(n):
                if assignment.get(var,'') == val: ch ='*'
                else: ch = ' '
                print str(self.nconflicts(var, val, assignment))+ch,
            print    
    
    def constraint(self,A, a, B, b):
         return A == B or (a != b and A + a != B + b and A - a != B - b)
     
        


class mapColoringProblem(csp):
    
    
    def __init__(self):
        mapColoringVariables=["SA","WA","NT", "Q" ,"NSW","V","T"]
    
        domains={}
        for var in mapColoringVariables:
            domains[var]=["R","G","B"]
        
        neighbors={
                
                "SA":[ "WA","NT","Q","NSW","V"],
                "NT": ["WA","Q","SA"],
                "NSW":["Q","V","SA"],
                "WA":["NT","SA"],
                "Q":["NT","SA","NSW"],
                "V":["NSW","SA"]    ,
                "T": ""  
            }

        
        csp.__init__(self, mapColoringVariables, domains, neighbors,self.constraint)
    
    def constraint(self,A, a, B, b):
        
       
    #A constraint saying two neighboring variables must differ in value."
        return a != b




class sudokuProblem(csp):
    def __init__(self,grid):
        cols = "123456789"
        rows = "ABCDEFGHI"
        def cross(A, B):
        	return [a + b for a in A for b in B]
        
        self.variables = cross(rows, cols)
        domain = self.getDict(grid)
        
        
        
        unitlist = ([cross(rows, c) for c in cols] +
           [cross(r, cols) for r in rows] +
           [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        units = dict((s, [u for u in unitlist if s in u]) for s in self.variables)
        self.nieghbors = dict((s, list(set(sum(units[s],[]))-set([s]))) for s in self.variables)
      
        #constraint = {(variable, peer) for variable in self.variables for peer in self.peers[variable]}
        
      
        csp.__init__(self, self.variables, domain,self.nieghbors, self.constraint)
        
    def constraint(self,A, a, B, b):
        
        if a==b:
            return False
        partialDomain={}
      
        for i in self.nieghbors[B]:
            if len(self.curr_domains[i]) ==1:
                partialDomain[i]=self.curr_domains[i]
                for j in partialDomain[i]:
                    if j==b :
                        return False
            
    
        
        return True
    
        
    def getDict(self, grid=""):
        
                i = 0
               
                values = dict()
                for cell in self.variables:
                    if grid[i]!='0':
                        values[cell] = [grid[i]]
                    else:
                        values[cell] = range(1,10)
                    i = i + 1
                return values
    def display(self,values):
        cols = "123456789"
        rows = "ABCDEFGHI"
        for r in rows:
            
            s=""
            for c in cols:
                
                s=s+"\t"+str(values[r+c] )
            print s, "\n"

 