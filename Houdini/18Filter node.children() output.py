#Filter node.children() output
import hou
selectedNode = hou.selectedNodes()

def extractVop(listOfChildrens):
    for node in listOfChildrens:
        if node.type().name() == 'vopsurface':
            return node

# return vopsurface nodes
vops = extractVop(selectedNode.children())