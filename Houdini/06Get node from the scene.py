#Get node from the scene
import hou
node = hou.node('/<nodePath>/<nodeName>') # By name
node = hou.selectedNodes()[0] # By selection
# Get node content
node.children()

#Get node upstream connections
listParents = node.inputAncestors()