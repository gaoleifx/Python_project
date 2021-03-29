#Create Material Stylesheet UI
# Create Material Stylesheet parameter interface
# Select Geometry node, run script

import hou

# Get selected geometry node to create Stylesheet parameter
OBJ = hou.selectedNodes()[0]

# Define tags
dataTags = {'script_action_icon':'DATATYPES_stylesheet',
            'script_action_help':'Open in Material Style Sheet editor.',
            'spare_category':'Shaders',
            'script_action':"import toolutils\np = toolutils.dataTree('Material Style Sheets')\np.setCurrentPath(kwargs['node'].path() + '/Style Sheet Parameter')",
            'editor':'1'}

# Create parameter interface
group = OBJ.parmTemplateGroup()
folder = hou.FolderParmTemplate('folder', 'Shaders')
folder.addParmTemplate(hou.StringParmTemplate('shop_materialstylesheet', 'Material Style Sheet', 1, tags = dataTags))
group.append(folder)
OBJ.setParmTemplateGroup(group)