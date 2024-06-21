import bpy
from mathutils import Vector

# Obtenir les objets nommés "Empty"
obj1 = bpy.data.objects.get("Empty.001")
obj2 = bpy.data.objects.get("Empty.002")

if obj1 and obj2:
    # Obtenir les positions des objets
    pos1 = obj1.location
    pos2 = obj2.location
    
    # Calculer la distance entre les deux positions
    distance = (pos2 - pos1).length
    print(f"La distance entre les deux objets est de {distance:.4f} unités")
else:
    print("Un ou les deux objets nommés 'Empty' n'ont pas été trouvés")
    
output_file_path = "C:/Users/Nathan/Documents/Projet/ModelisationForMR/TP/TP3/distance.txt"
with open(output_file_path, 'w') as f:
    f.write(f"La distance entre les deux objets est de {distance:.4f} unités")
