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
        
        
        csp.__init__(self, variabels, domain,
                     nieghbors, self.constraint)

    def display(self, assignment):
        
        n = len(self.variables)
        for val in range(n):
            for var in range(n):
                if assignment.get(var,'') == val: ch ='Q'
                elif (var+val) % 2 == 0: ch = '*'
                else: ch = '.'
                print ch,
            print '    ',
            
           
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



