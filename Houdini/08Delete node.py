#Delete node
import hou
node = hou.node('/<nodePath>/<nodeName>')
node.destroy() # Delete node