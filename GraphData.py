# Author:  jycwsf@github
# Copyright (C) 2017
# All rights reserved

class GraphData:
    def __init__(self, src):
        lines = src.strip().split('\n')
        self.nodes = [] # list of nodes
        self.edges = [] # list of (Node, Node, Weight)
        for line in lines:
            if line.startswith('#'):
                continue # skip a comment line
            columns = line.split()
            if len(columns) < 3:
                print("[Warning] unrecoginized line %s. (Expected to be 'Node Node Weight')")
                continue
            for n in columns[0:2]:
                if n not in self.nodes:
                    self.nodes.append(n)
            self.edges.append(columns[0:3])

    
    def graphvizView(self):
        # assume graphviz (https://pypi.python.org/pypi/graphviz and http://www.graphviz.org/) is installed.
        if not self.edges:
            return
        from graphviz import Graph
        g = Graph('Graph')
        for e in self.edges:
            # print(e)
            g.edge(*e)
        #print(g.source)
        g.view()

def test():
    data = '''# Node Node EdgeWeight
A B 1
A C 1
A D 1
B C 1
B E 1
C F 1
'''
    # g = GraphData(data)
    # g.graphvizView()
    with open("./data/graph1.txt") as f:
        g = GraphData(data)
        g.graphvizView()

if __name__ == "__main__":
  test()
