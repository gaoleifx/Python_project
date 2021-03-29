#Get Translate X keyframes of selected node
import hou
node = hou.selectedNodes()[0]

node.parm('tx').keyframes()