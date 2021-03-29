#Get all node parameters names
def getAllNodeParameters(node):
    # Return list of all parameters names for input node object 
    allParameters = [param.name()for param in node.parms()]
    return allParameters 