# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:13:59 2019

@author: Fte
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:19:47 2019

@author: Fte
"""

from BacktrackingImplentiano import  AC3,count_if

class csp:
    
    def __init__ (self,variables, domains,neighbors ,constraint):
        self.variables = variables
        self.domains = domains
        self.neighbors=neighbors
        
        self.currentDomain =None
        self.constraint=constraint

    def assign (self, var, val, assignment):
     
        assignment[var] = val
                      
                  
        AC3(self, [(Xk, var) for Xk in self.neighbors[var]])
      
            
     
            
    def unassign(self, var, assignment):
        if  var in assignment:
            self.currentDomain[var] = self.domains[var][:]
                
            del assignment[var]
    def IsConsistente(self, var, val, assignment):
        def conflict(var2):
            val2 = assignment.get(var2, None)
            
            return val2 != None and not self.constraint(var, val, var2, val2)
        return count_if(conflict, self.neighbors[var])
         




 
    

    


    
    
    
    
    


    