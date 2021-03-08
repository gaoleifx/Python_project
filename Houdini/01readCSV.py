import csv
import os
import hou

node = hou.pwd()
geo = node.geometry()

######创建函数
def addPoints(pos, name, value, rotValue):
    point = geo.createPoint()
    point.setPosition(pos)
    attrib = geo.findPointAttrib(name)
    if attrib == None:
        if type(value) == str:
            attrib = geo.addAttrib(hou.attribType.Point, name, value)
        if type(value) == unicode:
            attrib = geo.addAttrib(hou.attribType.Point, name, value)
    if attrib != None:
        point.setAttribValue(attrib, value)
        
    rot = geo.findPointAttrib('rot')
    if rot == None:
        rot = geo.addAttrib(hou.attribType.Point, 'rot', rotValue)
    if rot != None:
        point.setAttribValue(rot, rotValue)
#print('-------------------------------------')

###读取csv文件
path = node.parm('path').evalAsString() + '/' + node.parm('filename').evalAsString()

with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    head_row = next(csv_reader)
    
    for row in csv_reader:
        preName = row[2]
        #print(type(preName))
        prePos = hou.Vector3(float(row[3]), float(row[4]), float(row[5]))
        preRot = hou.Vector3(float(row[6]), float(row[7]), float(row[8]))
        #print(type(preRot))
        point = addPoints(prePos, "preName", preName, preRot)