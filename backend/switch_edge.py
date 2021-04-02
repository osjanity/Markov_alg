def switch_edge(x, y):
    '''
    switches the edge (x,y) to (y,x)
    x, y: NodeData
    '''

    # preparation:
    # use itertools.product to get all possible assignments of values for the parent nodes:

    all_possible_parent_assignments = list(itertools.product([0,1], repeat=x.num_parents))
    num_parents_assigments = len(all_possible_parent_assignments)

    # get conditional joint distribution p(x,y | parents):
    # initialization:
    pxe0ye0 = [0 for _ in range(2**x.num_parents)]
    pxe0ye1 = [0 for _ in range(2**x.num_parents)]
    pxe1ye0 = [0 for _ in range(2**x.num_parents)]
    pxe1ye1 = [0 for _ in range(2**x.num_parents)]


    # iterate through all possible assignments for the common parents of x and y:
    for a_i in range(num_parents_assigments):

        assignemnt_dict_x = {x.parents[i] : all_possible_parent_assignments[a_i][i] for i in range(x.num_parents)}
        assignemnt_dict_y = {x.parents[i] : all_possible_parent_assignments[a_i][i] for i in range(x.num_parents)}

        ## O(c)
        assignemnt_dict_y[x.name] = 0

        # case x=0, y=1:
        pxe0ye1[a_i] = (1-x.get_conditional(assignemnt_dict_x)) * y.get_conditional(assignemnt_dict_y)
        # case x=0, y=0:
        pxe0ye0[a_i] = (1-x.get_conditional(assignemnt_dict_x)) * (1-y.get_conditional(assignemnt_dict_y))

        assignemnt_dict_y[x.name] = 1

        # case x=1, y=1:
        pxe1ye1[a_i] = x.get_conditional(assignemnt_dict_x) * y.get_conditional(assignemnt_dict_y)
        # case x=1, y=0:
        pxe1ye0[a_i] = x.get_conditional(assignemnt_dict_x) * (1-y.get_conditional(assignemnt_dict_y))

    # marginalize x from the conditional distribution of y:
    pye0 = [pxe0ye0[i] + pxe1ye0[i] for i in range(num_parents_assigments)]
    pye1 = [pxe0ye1[i] + pxe1ye1[i] for i in range(num_parents_assigments)]

    # condition x on the possible values of y:
    pxe0gye0 = [pxe0ye0[i]/pye0[i] for i in range(num_parents_assigments)]
    pxe0gye1 = [pxe0ye1[i]/pye1[i] for i in range(num_parents_assigments)]
    pxe1gye0 = [pxe1ye0[i]/pye0[i] for i in range(num_parents_assigments)]
    pxe1gye1 = [pxe1ye1[i]/pye1[i] for i in range(num_parents_assigments)]

    x_new_parents = [y.name]
    if not x.parents == None:
        x_new_parents += x.parents
    x_new = NodeData(x.name, parents=x_new_parents)

    for a_i in range(num_parents_assigments):
        assignment_dict = {x.parents[i] : all_possible_parent_assignments[a_i][i] for i in range(x.num_parents)}
        assignment_dict[y.name] = 0
        x_new.set_conditional(p=pxe1gye0[a_i], parent_assignment=assignment_dict)
        assignment_dict[y.name] = 1
        x_new.set_conditional(p=pxe1gye1[a_i], parent_assignment=assignment_dict)

    y_new_parents = []

    if not x.parents == None:
        y_new_parents += x.parents

    y_new = NodeData(y.name, parents=y_new_parents)

    for a_i in range(num_parents_assigments):
        # construct the assignment-dictionary:
        assignment_dict = {x.parents[i] : all_possible_parent_assignments[a_i][i] for i in range(x.num_parents)}
        y_new.set_conditional(p=pye1[a_i], parent_assignment=assignment_dict)

    return x_new, y_new
