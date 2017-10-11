import pydot


def drawEdge(graph, parent, child):
    edge = pydot.Edge(parent, child)
    graph.add_edge(edge)


def drawTree(graph, node, parent=None):
    for key, value in node.items():
        if isinstance(value, dict):
            if parent:
                drawEdge(graph, parent, key)
            drawTree(graph, value, key)
        else:
            drawEdge(graph, parent, key)
            graph.add_node(pydot.Node(key + '_' + value, label=value))
            drawEdge(graph, key, key + '_' + value)
