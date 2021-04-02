
# get thing from json request
# parse thing enough to put into this class
# #use the populated class to run algs (find_reversal, switch_edge)


import itertools
class NodeData:
    '''
    Attributes:
        parents: a list of strings that contains the names of the parent nodes
        conditionals: a list of size 2^p (where p is the number of parents)
            that contains the conditional probabilities of the random variables of this node given all possible values for the parents
    '''
    def __init__(self, name, parents=None, conditionals=None):
        self.name = name
        self.parents = parents

        # initializing the data structures,
        # mostly stuff that ensures that everything also works for nodes without parents
        if parents == None:
            self.num_parents = 0
        else:
            self.num_parents = len(self.parents)

        if conditionals == None:
            self.conditionals = [0 for _ in range(2**self.num_parents)]
        else:
            self.conditionals = conditionals


    def set_conditional(self, p, parent_assignment=None):
        '''
        parent_assignment: a dict that maps values to names of parents, e.g.
        {'x1' : 0, 'x2' : 1, 'x3' : 0, ...}
        this function computes the index of self.conditionals where the required value is stored and sets the conditional probability
        '''
        # handle special case of node without parents:
        if self.parents == None:
            self.conditionals[0] = p
            return
        # general case:
        index = 0
        for p_i in range(len(self.parents)):
            index += parent_assignment[self.parents[p_i]] * 2**p_i

        self.conditionals[index] = p


    def get_conditional(self, parent_assignment):
        '''
        parent_assignment: a dict that maps values to names of parents, e.g.
        {'x1' : 0, 'x2' : 1, 'x3' : 0, ...}
        this function computes the index of self.conditionals where the required value is stored and returns the conditional
        '''

        ##input of get conditionals is parent_assignment, dict which grows linearly with number of parents.
        ##So we can calculate this in terms of numparsx.

        # handle special case of node without parents:
        # O(c)
        if self.parents == None:
            return self.conditionals[0]
        # general case:
        #O(c)
        index = 0
        #multiplier of O(numparsx)
        for p_i in range(len(self.parents)):
            #O(numparsx)
            index += parent_assignment[self.parents[p_i]] * 2**p_i

        return self.conditionals[index]


    def print_conditionals(self):
        '''
        prints the full conditional distribution
        iterates through all possible assignments and prints the conditional distribution for each assignment in a seperate line
        '''
        all_possible_parent_assignments = [x for x in itertools.product([0,1], repeat=self.num_parents)]

        for a_i in range(2**self.num_parents):
            assignment = {self.parents[i] : all_possible_parent_assignments[a_i][i] for i in range(self.num_parents)}
            # some list-magic that produces a sufficiently nice string:
            assignment_string = "P("+self.name+" = 1 | " + ', '.join([str(x) + " = " + str(assignment[x]) for x in assignment]) + " ) = " + str(self.get_conditional(assignment))
            print (assignment_string)
