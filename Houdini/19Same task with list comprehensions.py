#Same task with list comprehensions:
import hou
selectedNode = hou.selectedNodes()

# return vopsurface nodes
vops = [node for node in selectedNode.children() if node.type().name() == 'vopsurface']