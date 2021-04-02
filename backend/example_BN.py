
# define graph:
x1 = NodeData('x1')
x1.set_conditional(p=0.8)

x2 = NodeData('x2', parents=['x1'])
x2.set_conditional(p=0.2, parent_assignment={'x1':0})
x2.set_conditional(p=0.4, parent_assignment={'x1':1})

x3 = NodeData('x3', parents=['x1', 'x2'])
x3.set_conditional(p=0.1, parent_assignment={'x1': 0, 'x2': 0})
x3.set_conditional(p=0.2, parent_assignment={'x1': 1, 'x2': 0})
x3.set_conditional(p=0.4, parent_assignment={'x1': 0, 'x2': 1})
x3.set_conditional(p=0.8, parent_assignment={'x1': 1, 'x2': 1})

x1.print_conditionals()
x2.print_conditionals()
x3.print_conditionals()

nodes = [x1,x2,x3]

G = nx.DiGraph()
G.clear()
G.add_edges_from([(x1, x2), (x2, x3),(x1,x3)]) # using a list of edge tuples
nx.draw(G)
plt.show()

## Specific to the query - find the best reversal and switch it
target = x2
conditions = []
x, y = best_reversal(G,target,conditions)
print("Best reversal:", x.name, y.name)

print ("switch edge (", x.name, ",", y.name, ")")
x_new, y_new = switch_edge(x, y)
x_new.print_conditionals()
y_new.print_conditionals()
G_new = structure_reverse_edge(G,x,y)
