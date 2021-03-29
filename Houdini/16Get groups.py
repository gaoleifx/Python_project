#Get groups
import hou

node = hou.selectedNodes()[0]
groups = [g.name() for g in node.geometry().primGroups()]
print groups