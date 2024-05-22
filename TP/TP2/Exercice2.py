import numpy as np
import trimesh
import networkx as nx
import Exercice1 as ex1

def transform_quad_to_tri(mesh):
    vertices, faces = mesh
    new_faces = []
    for face in faces:
        if len(face) == 4:
            new_faces.append([face[0], face[1], face[2]])
            new_faces.append([face[0], face[2], face[3]])
        else:
            new_faces.append(face)
    return vertices, new_faces

def generate_cube_mesh():
    vertices = np.array([
        [0, 0, 0], # 0
        [1, 0, 0], # 1
        [1, 1, 0], # 2
        [0, 1, 0], # 3
        [0, 0, 1], # 4
        [1, 0, 1], # 5
        [1, 1, 1], # 6
        [0, 1, 1], # 7
    ])

    edges = np.array([
        [0, 1, 2], [2, 3, 0], # Face inférieure
        [4, 5, 6], [6, 7, 4], # Face supérieure
        [0, 1, 5], [5, 4, 0], # Face avant
        [1, 2, 6], [6, 5, 1], # Face droite
        [2, 3, 7], [7, 6, 2], # Face arrière
        [3, 0, 4], [4, 7, 3]  # Face gauche
    ])

    mesh = (vertices, edges)
    return mesh

def generate_tetrahedron_mesh():
    vertices = np.array([
        [0, 0, 0], # 0
        [1, 0, 0], # 1
        [0.5, 1, 0], # 2
        [0.5, 0.5, 1], # 3
    ])

    faces = np.array([
        [0, 1, 2],
        [0, 1, 3],
        [1, 2, 3],
        [2, 0, 3],
    ])

    mesh = (vertices, faces)
    return mesh

def generate_teseract_mesh():
    vertices = np.array([
        [0, 0, 0], # 0
        [1, 0, 0], # 1
        [1, 1, 0], # 2
        [0, 1, 0], # 3
        [0, 0, 1], # 4
        [1, 0, 1], # 5
        [1, 1, 1], # 6
        [0, 1, 1], # 7
    ])

    faces = np.array([
        [0, 1, 2], [0, 2, 3], # Face inférieure
        [4, 5, 6], [4, 6, 7], # Face supérieure
        [0, 1, 5], [0, 5, 4], # Face avant
        [1, 2, 6], [1, 6, 5], # Face droite
        [2, 3, 7], [2, 7, 6], # Face arrière
        [3, 0, 4], [3, 4, 7], # Face gauche
    ])

    mesh = (vertices, faces)
    return mesh

def generate_cube_hole_mesh():
    vertices = np.array([
        [0, 0, 0], # 0
        [1, 0, 0], # 1
        [1, 1, 0], # 2
        [0, 1, 0], # 3
        [0, 0, 1], # 4
        [1, 0, 1], # 5
        [1, 1, 1], # 6
        [0, 1, 1], # 7
        [0.5, 0.25, 0], # 8
        [0.5, 0.75, 0], # 9
        [0.5, 0.75, 1], # 10
        [0.5, 0.25, 1], # 11
    ])

    faces = np.array([
        [0, 1, 8], [1, 9, 8], # Face inférieure
        [4, 5, 11], [5, 10, 11], # Face supérieure
        [0, 1, 5], [0, 5, 4], # Face avant
        [1, 2, 9], [2, 10, 9], # Face droite
        [2, 3, 6], [2, 6, 10], # Face arrière
        [3, 0, 4], [3, 4, 7], # Face gauche
        [8, 9, 10], [8, 10, 11], # Trou
    ])

    mesh = (vertices, faces)
    return mesh

def loop_subdivision(mesh, iterations=1):
    vertices, faces = mesh

    for _ in range(iterations):
        # Étape 1: Ajouter des points au milieu de chaque arête
        edge_points = {}
        edge_set = set()
        new_vertices = list(vertices)
        for face in faces:
            for i in range(3):
                point1, point2 = sorted([face[i], face[(i+1)%3]])
                if (point1, point2) not in edge_set:
                    new_point = (vertices[point1] + vertices[point2]) / 2
                    edge_points[(point1, point2)] = len(new_vertices)
                    new_vertices.append(new_point)
                    edge_set.add((point1, point2))

        # Étape 2: Mettre à jour la position des points existants
        adjacency_graph = nx.from_edgelist(edge_points.keys())
        degrees = [adjacency_graph.degree(vertex) for vertex in range(len(vertices))]
        for vertex in range(len(vertices)):
            neighbors = list(adjacency_graph.neighbors(vertex))
            if len(neighbors) == degrees[vertex]: # Point intérieur
                n = degrees[vertex]
                beta = 3/16 if n == 3 else 3/(8*n)
                new_vertices[vertex] = (1 - n*beta)*vertices[vertex] + beta*sum(new_vertices[neighbor] for neighbor in neighbors)
            else: # Point sur le bord
                border_neighbors = [neighbor for neighbor in neighbors if adjacency_graph.degree(neighbor) < len(list(adjacency_graph.neighbors(neighbor)))]
                new_vertices[vertex] = 1/8 * sum(new_vertices[neighbor] for neighbor in border_neighbors) + 3/4 * vertices[vertex]

        # Étape 3: Relier tous les points ensemble
        new_faces = []
        for face in faces:
            points = [edge_points[tuple(sorted([face[i], face[(i+1)%3]]))] for i in range(3)]
            new_faces.append([face[0], points[0], points[2]])
            new_faces.append([face[1], points[1], points[0]])
            new_faces.append([face[2], points[2], points[1]])
            new_faces.append(points)

        vertices = np.array(new_vertices)
        faces = np.array(new_faces)

    return vertices, faces


if __name__ == '__main__':
    mesh = generate_cube_hole_mesh()
    mesh = transform_quad_to_tri(mesh)
    ex1.Visualize3DMesh(mesh[0], mesh[1])
    for i in range(5): # Changez ce nombre pour le nombre d'itérations que vous voulez
        print(f"Iteration {i+1}")
        new_mesh = loop_subdivision(mesh, 1)
        ex1.Visualize3DMesh(new_mesh[0], new_mesh[1])
        mesh = new_mesh
