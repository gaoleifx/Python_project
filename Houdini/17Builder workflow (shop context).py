#Builder workflow (shop context)
#Create "Material Surface Builder" in SHOP context, dive inside.
import hou
shader = hou.node('/shop/vopmaterial1/lambert1')
out = hou.node('/shop/vopmaterial1/surface_output')
out.setNamedInput('Cf', shader, 'clr') # Set connection by name
out.setNamedInput(0, shader, 0) # Set connection by parameter index

# List all inputs for node 'surface_output'
print out.inputNames()