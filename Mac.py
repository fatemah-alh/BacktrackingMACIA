# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:26:30 2019

@author: Fte
"""



from copy import deepcopy
def MACSearch(csp):
    
    csp.currentDomain = deepcopy(csp.domains)    
    return Mac({}, csp)


def Mac(assignment, csp):
    if isComplete(assignment,csp):
        return assignment
    var =SelectUnassignedVariables(assignment, csp)
    for val in orderDomainValues(var, assignment, csp):
        if csp.IsConsistente(var, val, assignment) == 0:
            csp.assign(var, val, assignment)
            result=Mac(assignment, csp)
            if result is not None:
                return result
        csp.unassign(var, assignment)
    return None

def AC3(csp, queue=None):    
    while queue:
        (Xi, Xj) = queue.pop()
        if rivesd(csp, Xi, Xj):
            for Xk in csp.neighbors[Xi]:
                queue.append((Xk, Xi))

def rivesd(csp, Xi, Xj):
    "Return true if we remove a value."
    removed = False
    for x in csp.currentDomain[Xi]:#xj is th var which ha valore value,
    #Xi is on niebore of Xj, x is one value from tha all domain of Xi
    #si deve eliminare il valore x se e uguale al valore vale che e stata assegnata a Xj
        
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        xIsConsistent=False
        for y in csp.currentDomain[Xj]:
            if csp.constraint(Xi,x,Xj,y):
                xIsConsistent=True
            
        if xIsConsistent==False:
            
            csp.currentDomain[Xi].remove(x)
            removed = True
    return removed


#CHECKS IF THE ASSIGNMENT IS COMPLETE
def isComplete(assignment,csp):
	return set(assignment.keys())==set(csp.variables)



#SELECTS THE NEXT VARIABLE TO BE ASSIGNED USING MRV
def SelectUnassignedVariables(assignment, csp):
	unassigned_variables = dict((var, len(csp.currentDomain[var])) for var in csp.currentDomain if var not in assignment.keys())
	mrv = min(unassigned_variables, key=unassigned_variables.get)
	return mrv


def orderDomainValues(var, assignment, csp):
    "Decide what order to consider the domain variables."
   
    return csp.currentDomain[var] 




#CHECKS IF THE GIVEN NEW ASSIGNMENT IS CONSISTENT
def isConsistent(var, value, assignment, csp):       
    	for neighbor in csp.neighbors[var]:            
            if neighbor in assignment.keys() and assignment[neighbor]==value:
        			return False
    	return True


def count_if(predicate, seq):
    """Count the number of elements of seq for which the predicate is true.
    
    """
    f = lambda count, x: count + (not not predicate(x))
    return reduce(f, seq, 0)
