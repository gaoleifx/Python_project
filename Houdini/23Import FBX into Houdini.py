import hou
import os 

dirFBX = 'P:/PROJECTS/NSI/PROD/3D/lib/ANIMATION/CHARACTERS/ROMA/FBX/' 
filesNamesFBX = [fileName for fileName in os.listdir(dirFBX) if os.path.isfile(os.path.join(dirFBX, fileName))]

for fileName in filesNamesFBX:
    fileFBX =  '{0}{1}'.format(dirFBX,fileName)
    if not hou.node('/obj/{}_fbx'.format(fileName.replace('.fbx',''))):
        hou.hipFile.importFBX(fileFBX) 
    else:
        print 'FBX {} EXISTS!'.format(fileName)