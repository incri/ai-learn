import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

class PPjGraph:
    def __init__(self, maxNodes):
        self.maxNodes = maxNodes
        self.nodes = []
        self.edges = np.array([[0] * maxNodes] * maxNodes)
    
    def addNode(self, node):
        if len(self.nodes) >= self.maxNodes:
            print('Max no. of nodes reached.')
        else:
            self.nodes.append(node)
        
    def addEdge(self, frm, to, weight):      
        fromIndex = self.nodes.index(frm)
        toIndex = self.nodes.index(to)
        
        self.edges[fromIndex][toIndex] = weight
    
    def successor(self, frm):
        succ = []
        
        fromIndex = self.nodes.index(frm)
        
        for idx, value in np.ndenumerate(self.edges[fromIndex]):
            if value > 0:
                succ.append(self.nodes[idx[0]])
        return succ
    
    def predecessor(self, to):
        pred = []
        
        toIndex = self.nodes.index(to)
        
        for idx, value in np.ndenumerate(self.edges[:,toIndex]):
            if value > 0:
                pred.append(self.nodes[idx[0]])
        return pred
    
    # Reference: 
    # https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
    def plotGraph(self):
        g = nx.DiGraph()
        for frmNode in self.nodes:
            frmIdx = self.nodes.index(frmNode)
            for toNode in self.nodes:                
                toIdx = self.nodes.index(toNode)
                if self.edges[frmIdx][toIdx] > 0:
                    g.add_edge(frmNode, 
                               toNode, 
                               weight = self.edges[frmIdx][toIdx])
        
        pos = nx.spring_layout(g, seed=8)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(g, 
                               pos, 
                               node_size=700)

        # edges
        nx.draw_networkx_edges(g, 
                               pos, 
                               width=3,
                               connectionstyle='arc3, rad = 0.1')

        # node labels
        nx.draw_networkx_labels(g, 
                                pos, 
                                font_size=20, 
                                font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(g, "weight")
        nx.draw_networkx_edge_labels(g, 
                                     pos, 
                                     edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()