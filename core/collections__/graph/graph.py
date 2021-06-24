
"""
    graph.py

    useful graph collection

    author: @alexzander
"""


# python
import os

# core package
from core.system import *
from core.json__ import *
from core.__collections.graph.exceptions import *
from core.path__ import *
# from exceptions import * (same thing, it works)


class Graph:
    def __init__(self, edges_json: list):
        self.nodes = []
        self.graph_adj_dict = {}
        self.edges = list(map(tuple, edges_json))

        for edge in edges_json:
            if edge[0] in self.graph_adj_dict:
                self.graph_adj_dict[edge[0]].append(edge[1])
            else:
                self.graph_adj_dict[edge[0]] = [edge[1]]
                self.nodes.append(edge[0])


    def degree(self, node: int):
        for __node, adj_nodes in self.graph_adj_dict.items():
            if __node == node:
                return len(adj_nodes)
        raise VertexNotFoundError


    def get_adj_list_represenation(self):
        graph_representation = ""
        for index, vertex in enumerate(self.graph_adj_dict.keys()):
            if index == len(self.graph_adj_dict.keys()) - 1:
                graph_representation += "{} -> {}".format(vertex, self.graph_adj_dict[vertex])
            else:
                graph_representation += "{} -> {}\n".format(vertex, self.graph_adj_dict[vertex])
        return graph_representation


    def __str__(self):
        return self.get_adj_list_represenation()