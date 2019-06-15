# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:26:30 2019

@author: Fte
"""



from copy import deepcopy
def BacktrackingSearch(csp):
    
    csp.curr_domains = deepcopy(csp.domains)
    
    
    return BacktrackMac({}, csp)




#THE RECURSIVE FUNCTION WHICH ASSIGNS VALUE USING BACKTRACKING 
def BacktrackMac(assignment, csp):
    if isComplete(assignment,csp):
        return assignment
    var =Select_Unassigned_Variables(assignment, csp)
    
    for val in order_domain_values(var, assignment, csp):
        if csp.nconflicts(var, val, assignment) == 0:
            csp.assign(var, val, assignment)
            result=BacktrackMac(assignment, csp)
            if result is not None:
                return result
        csp.unassign(var, assignment)
    return None

    

def AC3(csp,assignment, queue=None):
    
    while queue:
        (Xi, Xj) = queue.pop()
        if remove_inconsistent_values(csp, Xi, Xj):
            for Xk in csp.neighbors[Xi]:
                queue.append((Xk, Xi))

def remove_inconsistent_values(csp, Xi, Xj):
    "Return true if we remove a value."
    removed = False
    for x in csp.curr_domains[Xi]:#xj is th var which ha valore value,
    #Xi is on niebore of Xj, x is one value from tha all domain of Xi
    #si deve eliminare il valore x se e uguale al valore vale che e stata assegnata a Xj
        
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        xIsConsistent=False
        for y in csp.curr_domains[Xj]:
            if csp.constraint(Xi,x,Xj,y):
                xIsConsistent=True
            
        if xIsConsistent==False:
            
            csp.curr_domains[Xi].remove(x)
            removed = True
    return removed


#CHECKS IF THE ASSIGNMENT IS COMPLETE
def isComplete(assignment,csp):
	return set(assignment.keys())==set(csp.variables)



#SELECTS THE NEXT VARIABLE TO BE ASSIGNED USING MRV
def Select_Unassigned_Variables(assignment, csp):
	unassigned_variables = dict((var, len(csp.curr_domains[var])) for var in csp.curr_domains if var not in assignment.keys())
	mrv = min(unassigned_variables, key=unassigned_variables.get)
	return mrv


def order_domain_values(var, assignment, csp):
    "Decide what order to consider the domain variables."
    if csp.curr_domains:
        domain = csp.curr_domains[var]
    else:
        domain = csp.domains[var][:]
    return domain
#RETURNS THE STRING OF VALUES OF THE GIVEN VARIABLE 
def Order_Domain_Values(var, assignment, csp):
	return csp.domains[var]



#CHECKS IF THE GIVEN NEW ASSIGNMENT IS CONSISTENT
def isConsistent(var, value, assignment, csp):       
    	for neighbor in csp.neighbors[var]:            
            if neighbor in assignment.keys() and assignment[neighbor]==value:
        			return False
    	return True


def count_if(predicate, seq):
    """Count the number of elements of seq for which the predicate is true.
    >>> count_if(callable, [42, None, max, min])
    2
    """
    f = lambda count, x: count + (not not predicate(x))
    return reduce(f, seq, 0)
