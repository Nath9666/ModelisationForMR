import numpy as np
import polyscope as ps
import uuid
import os

def Load_off(file_OFF:str)-> tuple:
    """
    Loads a .off file and returns the vertices and faces as numpy arrays.

    Parameters:
    file_OFF (str): The path to the .off file.

    Returns:
    tuple: A tuple containing two numpy arrays. The first array represents the vertices and the second array represents the faces.

    Raises:
    ValueError: If the file is not a .off file, does not exist, or is empty.
    """
    if file_OFF[-4:] != '.off':
        raise ValueError('The file is not a .off file')
    if not os.path.exists(file_OFF):
        raise ValueError('The file does not exist')
    if os.path.getsize(file_OFF) == 0:
        raise ValueError('The file is empty')
    with open(file_OFF, 'r') as f:
        lines = f.readlines()
        vertices = []
        faces = []
        for line in lines:
            if line[0] == 'v':
                vertices.append([float(i) for i in line.split()[1:]])
            elif line[0] == 'f':
                faces.append([int(i) for i in line.split()[1:]])
    return np.array(vertices), np.array(faces)

def Load_Obj(file_Obj:str)-> tuple:
    """
    Loads a .obj file and returns the vertices and faces as numpy arrays.

    Parameters:
    file_Obj (str): The path to the .obj file.

    Returns:
    tuple: A tuple containing two numpy arrays. The first array represents the vertices and the second array represents the faces.

    Raises:
    ValueError: If the file is not a .obj file, does not exist, or is empty.
    """
    if file_Obj[-4:] != '.obj':
        raise ValueError('The file is not a .obj file')
    if not os.path.exists(file_Obj):
        raise ValueError('The file does not exist')
    if os.path.getsize(file_Obj) == 0:
        raise ValueError('The file is empty')
    with open(file_Obj, 'r') as f:
        lines = f.readlines()
        vertices = []
        faces = []
        for line in lines:
            if line[0] == 'v':
                vertex = [float(i) for i in line.split()[1:]]
                if len(vertex) < 3:  # Assuming 3D vertices
                    vertex.extend([0.0] * (3 - len(vertex)))
                vertices.append(vertex)
            elif line[0] == 'f':
                face = [int(i.split('/')[0]) - 1 for i in line.split()[1:]]  # Decrement face indices by 1
                if len(face) < 3:  # Assuming 3D faces
                    face.extend([0] * (3 - len(face)))
                faces.append(face)
    max_face_len = max(len(face) for face in faces)
    faces = [face + [0]*(max_face_len-len(face)) for face in faces]
    return np.array(vertices, dtype=float), np.array(faces, dtype=int)

def Visualize3DMesh(Vertices, Triangles):
    """
    Visualizes a 3D mesh represented by a set of vertices and its topology (triangles).

    Parameters:
    Vertices (np.array): The vertices of the 3D mesh.
    Triangles (np.array): The triangles of the 3D mesh.
    """
    ps.init()
    ps_mesh = ps.register_surface_mesh(str(uuid.uuid4()), Vertices, Triangles)
    ps.show()

def Visualize3DCurve(Vertices, Edges):
    """
    Visualizes a 3D curve represented by a set of vertices and its topology (edges).

    Parameters:
    Vertices (np.array): The vertices of the 3D curve.
    Edges (np.array): The edges of the 3D curve.
    """
    ps.init()
    for edge in Edges:
        if len(edge) < 2:
            raise ValueError('Edges must have at least 2 vertices')
        if len(edge) > 2:
            raise ValueError('Edges must have at most 2 vertices')
    ps_curve = ps.register_curve_network(str(uuid.uuid4()), Vertices, Edges)
    ps.show()

def main():
    # Load the .off file
    vertices, faces = Load_Obj('C:\\Users\\Nathan\\Documents\\Projet\\ModelisationForMR\\common-3d-test-models-master\\data\\alligator.obj')
    Visualize3DMesh(vertices, faces)

if __name__ == '__main__':
    main()