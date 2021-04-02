import NodeData from .BN_encoder
import itertools


#######################

example_json_structure = {
    "nodes": [
        {
            "name": "x3"
            "parents": [],
            "p": 0.5
        }
        {
            "name": "x1"
            "parents": ["x2", "x3"],
            "conditionals": [
                {
                    "p": 0.1,
                    "parent_assignment": { "x2": 1 "x3": 0}
                }
            ]
        }
    ]
}

def parse_data_structure(json_structure):
    nodes = []
    G = nx.DiGraph()

    # Add Nodes
    for node_def in json_structure["nodes"]:
        node = NodeData(node_def["name"], parents=node_def['parents'])

        for conditional in node_def['conditionals']:
            node.set_conditional(
                p=conditional["p"],
                parent_assignment=conditional.get("parent_assignment")
            )
        G.add_node(node)

    # Edges
    for node_def in json_structure["nodes"]:
        for parent in node['parents']:
            G.add_edge(G.node[parent], node)
    return G
