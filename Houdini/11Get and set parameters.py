#Get and set parameters
import hou
node = hou.selectedNodes()[0]

# get translate X
node.parm('tx').eval() 
hou.parm('/obj/geo1/tx').eval()
hou.ch('/obj/geo1/tx')

# Get string parameter without token evaluation
node = hou.node('/obj/geometry/fileCache')
print node.parm('file').eval() 
print node.parm('file').rawValue() 
# >> C:/temp/myFile.1.bgeo.sc
# >> $HIP/myFile.$F.bgeo.sc

# set translate XYZ
node.parmTuple('t').set([0,1,0])
hou.parm('/obj/geo1/tx').set(2)

# Set parameters for selected Remesh SOP
remesh = hou.selectedNodes()[0]
remesh.setParms({'group': 'myGroup', 'element_sizing1': 1, 'iterations': 2})