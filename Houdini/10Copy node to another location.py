#Copy node to another location
import hou
node = hou.node('/<nodePath>/<nodeName>')
parent = hou.node('/<parentPath>/')
hou.copyNodesTo([node], parent)