
from core.__collections.graph.graph import *


# TESTING
if __name__ == '__main__':
    cwd = os.getcwd()
    print(cwd)
    sep = get_path_sep(cwd)
    if cwd.endswith("core{}__collections{}graph".format(*([sep] * 2))):
        edges_path = "edges.json"
    else:
        edges_path = "D:/Alexzander__/programming/python/core/__collections/graph/edges.json"
        
    edges_json = read_json_from_file(edges_path)
    g = Graph(edges_json)
    print(g)