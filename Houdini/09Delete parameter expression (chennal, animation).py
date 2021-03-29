#Delete parameter expression (chennal, animation)
import hou
node = hou.node('/<nodePath>/<nodeName>')
node.parm(<parameterName>).deleteAllKeyframes()