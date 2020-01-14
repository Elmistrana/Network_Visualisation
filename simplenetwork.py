from pyvis.network import Network
import networkx as nx

ngraph = nx.complete_graph(40)
net= Network()
net.from_nx(ngraph)

nodes=[]

for node in range(1-40):
    nodes.append(node)

for n in range(len(nodes)):
    net.add_node(1, label= "Node"+  n)

#net.enable_physics(True)
net.show("mygraph.html")
