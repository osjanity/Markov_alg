## Helper function for find_case()
## O(number_ancestors(Y)) ? Needs to find the set nx.ancestors, presumably by checking edges (therefore parents),
## then check whether X is in that set. Should scale with the number of parents of the node linearly, ie if node has
## n parents, the check occurs n times.

def is_ancestor(G,X,Y): #checks whether X is an ancestor of Y
    if X in nx.ancestors(G,Y):
        return(1)

## Helper function for find_case()
## checks for paths between targets and parents of conditions.
def check_paths(G,X,Y,cases):
    skeleton = G.to_undirected()
    y_ancestors = list(nx.ancestors(G,Y))
    paths = list(nx.all_simple_paths(skeleton, X, Y, cutoff=None)) #use skeleton so they are undirected (routes not paths).

    if len(y_ancestors) == 0:
        cases[Y] = "special" #Yj in TRIVIAL SPECIAL CASE
        return(cases)

    # The logic of the following is to find paths from X to Y: if any of them pass through an ancestor of Y
    # then there is a "back route" to Y through its ancestors, meaning there is a path connecting X to a(Y)
    # which does not pass through Y.
    for path in paths:
        for y_ancestor in y_ancestors:
            if y_ancestor in path: #There exists a path from X to a(Y) which does not pass through Y
                cases[Y] = "general" #Yj IN GENERAL CASE
                return(cases)
            else:
                continue

    #Only reaches this block of code if all paths to a(Y) passed through Y; in nontrivial special case.
    cases[Y] = "special" #Yj IN SPECIAL CASE
    return(cases)

    ## Determine which case a query p(X|Ys) on a graph is in. Return the set of nodes the query depends on.
def find_case(G,X,Ys): #Graph G, one target Xf, set of multiple conditions Ys = {y0, y1, ...}
    ## O(c*edges(G)), probably.
    skeleton = G.to_undirected()

    ## O(c)
    dependent = []
    cases = {} #Dictionary with (key, value) pairs: (Y,case).
    if not nx.is_connected(skeleton): #Only consider connected graphs.
        return(0)
    if len(Ys) == 0:
        return(list(nx.ancestors(G,X)))

    ## O(check paths(Ys))
    for Y in Ys:
        cases = check_paths(G,X,Y,cases)

    ## O(shortest path) = n**2 logn +nm according according to NetworkXreference (but this is using weighted edges?),
    ## where n is number of nodes, m is number of edges
    shortest_path = nx.shortest_path(skeleton,X,Y) #use skeleton so we have shortest route (undirected)
    x_ancestors = list(nx.ancestors(G,X))
    y_ancestors = list(nx.ancestors(G,Y))

    ## O(number of ancestors of x)
    dependent.append(X)
    for x_ancestor in x_ancestors:
        dependent.append(x_ancestor)

    ## O (len(Ys)
    for Y in Ys:
        if cases[Y] == "general":
            for node in shortest_path:
                dependent.append(node) ##Includes all nodes on shortest route form X to Y including X and Y.
            for y_ancestor in y_ancestors:
                dependent.append(y_ancestor)

        if cases[Y] == "special":
            for node in shortest_path:
                dependent.append(node)
            dependent = list(set(dependent))
            dependent.remove(Y)
            for y_ancestor in y_ancestors:
                if y_ancestor in dependent:
                    dependent.remove(y_ancestor)

    return(list(set(dependent)))

    ## Return the set of covered edges in a graph. Independent of query.

# O (number_edges, number of predeccors of x, number of predeccesors y)
## ^ growth of these with number of nodes depends on the type of graph...

def find_covered_edges(G):
    ## O(c)
    covered_edges = []
    ## O(number_edges)
    for edge in G.edges: #for edge (X,Y)
        # O(number of predecessorsx + number of predeccors y) + c
        source_parents = list(G.predecessors(edge[0])) #parents of X
        target_parents = list(G.predecessors(edge[1])) #parents of Y
        source_parents.append(edge[0]) #parents of X union X
        if set(source_parents) == set(target_parents):
            covered_edges.append(edge)
    return(covered_edges)

## Reverse chosen edge of a graph (only structurally, not probabilities), return altered graph

## O(G.copy) + c
def structure_reverse_edge(G, x, y):
    Grev = G.copy()
    Grev.add_edge(y,x)
    Grev.remove_edge(x,y)
    return(Grev)

    ## Given a query p(X|Ys), determine whether switching covered edge is advantageous,
## and return the number of vertices which no longer need to be computed given a possible switch
def is_advantageous(G,edge, X, Ys):
    vertex_cost_difference = 0
    cost_before = len(find_case(G, X, Ys))

    x = edge[0]
    y = edge[1]
    Grev = G.copy()
    Grev = structure_reverse_edge(Grev,x,y)
    cost_after = len(find_case(Grev,X,Ys))
    if cost_after < cost_before:
        vertex_cost_difference = cost_before - cost_after
    return(vertex_cost_difference)

    ## Iterates through covered edges and returns the covered edge for which
## reversal reduces the number of vertices which must be computed MOST at a given time.
def best_reversal(G, X, Ys):
    covered_edges = find_covered_edges(G)
    edge_advantages = {}
    for edge in covered_edges:
         edge_advantages[edge] = is_advantageous(G,edge,X,Ys)
    max_adv_edge = max(edge_advantages, key=edge_advantages.get)
    return(max_adv_edge)
