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
        
        self.curr_domains=None
        self.constraint=constraint
	#INITIALIZING THE CSP
    def assign (self, var, val, assignment):
     
        assignment[var] = val
                      
                  
        AC3(self, assignment,[(Xk, var) for Xk in self.neighbors[var]])
      
            
          #  AC3(self, [(Xk, var) for Xk in self.neighbors[var]])
            
    def unassign(self, var, assignment):
        if  var in assignment:
            self.curr_domains[var] = self.domains[var][:]
                
            del assignment[var]
    def nconflicts(self, var, val, assignment):
        def conflict(var2):
            val2 = assignment.get(var2, None)
            
            return val2 != None and not self.constraint(var, val, var2, val2)
        return count_if(conflict, self.neighbors[var])
         



"""
class cryptProblem (csp):
    def __init__(self,):
        variables=["T","F","W","O","U","R","c1","c2","c3"]
        domain= {}
        nieghbors={}
        #nieghbors={"T":["O","c3","c2"],
        #           "F":["R","c1"]
        #        }
        
        for v in variables:
            if v == "T" or v=="F":
                domain[v]=range(1,10)
                #↨nieghbors[v]=["T","F","W","O","U","R"]
            domain[v]=range(0,10)
           # nieghbors[v]=["T","F","W","O","U","R"]
           
        
        csp.__init__(self, variables, domain,
                     nieghbors, self.constraint)
        
        def constraint(self,A,a,B,b):
            
            
            
"""        
        
        




#print solved2

 
    

    


    
    
    
    
    


    