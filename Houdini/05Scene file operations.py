#Scene file operations
import hou
sceneRoot = hou.node('/obj')

# Save current scene as file
hou.hipFile.save('C:/temp/myScene_001.hipnc')

# Export selected node to a file
sceneRoot.saveChildrenToFile(hou.selectedNodes(), [], 'C:/temp/nodes.hipnc')

# Import file to the scene
sceneRoot.loadChildrenFromFile('C:/temp/nodes.hipnc')