import numpy as np
import trimesh
import networkx as nx
import Exercice1 as ex1

def loop_subdivision(mesh, iterations=1):
    vertices, faces = mesh

    for _ in range(iterations):
        # Étape 1: Ajouter des points au milieu de chaque arête
        edge_points = {}
        new_vertices = list(vertices)
        for face in faces:
            for i in range(3):
                point1, point2 = sorted([face[i], face[(i+1)%3]])
                if (point1, point2) not in edge_points:
                    new_point = (vertices[point1] + vertices[point2]) / 2
                    edge_points[(point1, point2)] = len(new_vertices)
                    new_vertices.append(new_point)

        # Étape 2: Mettre à jour la position des points existants
        adjacency_graph = nx.from_edgelist(edge_points.keys())
        for vertex in range(len(vertices)):
            n = adjacency_graph.degree(vertex)
            beta = 3/16 if n == 3 else 3/(8*n)
            new_vertices[vertex] = (1 - n*beta)*vertices[vertex] + beta*sum(new_vertices[neighbor] for neighbor in adjacency_graph.neighbors(vertex))

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
    ex1.Visualize3DMesh(mesh[0], mesh[1])
    new_mesh = loop_subdivision(mesh, 5)
    ex1.Visualize3DMesh(new_mesh[0], new_mesh[1])
