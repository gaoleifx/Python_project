# Expand Alembic
# Recreate alembic hierarchy by object groups and names
# Select Alembic node, set 

# Naming convention
# Hirarchy in alembic: OBJECT (group)/PART_01, ..., PART_## (meshes)
# OBJECTS: <objectName>_<objectVariation> : bootle_A
# PARTS: <objectName>_<objectVariation>_<objectPart> : bootle_A_label

import hou
    
# Get Alembic SOP
ABC = hou.selectedNodes()[0]

def checkConditions():
    '''
    Check if environment conditions allows to run script without errors
    '''
    if not ABC:  # If user select anything
        print '>> Nothing selected! Select Alembic SOP!'
        return 0


def buildObjectsMap(listGroups):
    # Create object map dictionary: each object = key, list of parts = values
    
    objectsMap = {} # { OBJ: [PARTs] }
    
    for partNameFull in listGroups:
        items = partNameFull.split('_')
        object = '{0}_{1}'.format(items[0], items[1])
        part = items[2]
        
        if not object in objectsMap.keys():
            objectsMap[object] = [part]
        else:
            objectsMap[object].append(part)
    
    return objectsMap
        
def buildGroupsList(object, listParts):
    # Create string for BLAST SOP with list of groups for each object    

    groupsList = ''
    for part in listParts:
        name = '{}_{}'.format(object, part)
        groupsList += ' ' + name

    return groupsList
    
    

def expandABC(OBJ, objectsMap):
    # Recreate alembic hierarchy
    
    for object in sorted(objectsMap.keys()):             
        groupsList = buildGroupsList(object, objectsMap[object])
        blast = OBJ.createNode('blast')
        blast.setNextInput(ABC)
        blast.setName(object)
        blast.parm('group').set(groupsList)
        blast.parm('negate').set(1)
        blast.moveToGoodPosition()

def run():
    if checkConditions() != 0:    
        # Setup Alembic properties
        ABC.parm('loadmode').set(1) 
        ABC.parm('groupnames').set(4) 
        # Get Alembic container
        OBJ = ABC.parent()
        
        # Get all groups (PARTS) from alembic
        listGroups = [g.name() for g in ABC.geometry().primGroups()]
        
        # Build Objects Map
        objectsMap = buildObjectsMap(listGroups)
        # Expand Alembic
        expandABC(OBJ, objectsMap)
        
        print '>> EXPANDING DONE!'     
        
run()