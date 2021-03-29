#Create node in the scene
#To create any node wiyh Python you have to set parent node for that. You need to create Geometry node in OBJ context.
# Get scene root node
OBJ = hou.node('/obj/')
# Create Geometry node in scene root
geometry = OBJ.createNode('geo')


import hou
# Create transform node inside geo1
geometry = hou.node('/obj/geo1')
xform = geometry.createNode('xform') 
xform.moveToGoodPosition() # Align new node

# Create new transform node linked to existing transform
xformNew= xform.createOutputNode('xform')