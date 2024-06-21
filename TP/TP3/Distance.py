import bpy
import bmesh
from mathutils import Vector

# Get the active object
obj = bpy.context.active_object


# Ensure the object is in edit mode
if bpy.context.mode != 'EDIT_MESH':
    bpy.ops.object.mode_set(mode='EDIT')

# Create a BMesh representation of the object
bm = bmesh.from_edit_mesh(obj.data)

# Function to calculate distance between two vectors
def calculate_distance(v1, v2):
    return (v1 - v2).length

# Initialize total distance
total_distance = 0.0

# Iterate over all edges and sum their lengths
for edge in bm.edges:
    v1, v2 = edge.verts
    total_distance += calculate_distance(v1.co, v2.co)

# Switch back to object mode to apply the changes
bpy.ops.object.mode_set(mode='OBJECT')

# Free the BMesh
bm.free()



# Print the total distance
print(f"Total distance of the path: {total_distance:.4f}")

# Alternatively, write the result to a file
output_file_path = "C:/Users/Nathan/Documents/Projet/ModelisationForMR/TP/TP3/total_distance.txt"
with open(output_file_path, 'w') as f:
    f.write(f"Total distance of the path: {total_distance:.4f}\n")

# Report completion
print(f"Total distance has been written to {output_file_path}")
