# Exercice 2
1. Un maillage est dit "manifold" si chaque arête est partagée par exactement deux faces. Par exemple, un tétraèdre est un exemple de maillage triangulaire manifold. Un maillage non-manifold pourrait être un tétraèdre avec un triangle supplémentaire partageant une arête avec le reste du maillage.

2. Un maillage est dit "sans bord" si toutes ses arêtes sont partagées par deux faces. Par exemple, un tétraèdre est un maillage triangulaire sans bord. Un maillage avec bord pourrait être un triangle seul.

3. Une structure de données couramment utilisée pour représenter un maillage polygonal est une liste de sommets et une liste de faces. Chaque sommet est un point dans l'espace 3D, et chaque face est une liste d'indices dans la liste de sommets.
Exemple : 

```python
# Générer les coordonnées des sommets du cube
vertices = np.array([
    [0, 0, 0], # 0
    [1, 0, 0], # 1
    [1, 1, 0], # 2
    [0, 1, 0], # 3
    [0, 0, 1], # 4
    [1, 0, 1], # 5
    [1, 1, 1], # 6
    [0, 1, 1], # 7
    [0.5, 0.5, 0.5] # 8
])

# Générer les indices des arêtes du cube
edges = np.array([
    [0, 1], [1, 2], [2, 3], [3, 0], [0,2], # Face inférieure
    [4, 5], [5, 6], [6, 7], [7, 4], [4,6],  # Face supérieure
    # Ajouter les arêtes verticales
    [0, 4], [1, 5], [2, 6], [3, 7], [8, 0],
    [8, 1], [8, 2], [8, 3], [8, 4], [8, 5],
    [8, 6], [8, 7],
    # Ajouter les arêtes diagonales
    [0, 5], [1, 6], [2, 7], [3, 4]
])
```

4. Vous trouverez ci dessous la fonction ExtraireBord(M) qui permet de déterminer le bord d'un maillage M (en langage algorithmique puisen Python)
```
Début
    // Définir les coordonnées des sommets du cube
    sommets <- tableau de [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0.5, 0.5, 0.5]

    // Définir les indices des arêtes du cube
    aretes <- tableau de [0, 1], [1, 2], [2, 3], [3, 0], [0,2], [4, 5], [5, 6], [6, 7], [7, 4], [4,6], [0, 4], [1, 5], [2, 6], [3, 7], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [0, 5], [1, 6], [2, 7], [3, 4]
Fin
```

```python
def ExtraireBord(M):
    # M est un tuple (sommets, faces)
    sommets, faces = M
    aretes_faces = {}  # Dictionnaire pour garder une trace des faces qui contiennent chaque arête
    for i, face in enumerate(faces):
        for j in range(3):
            arete = tuple(sorted((face[j], face[(j+1)%3])))
            if arete in aretes_faces:
                aretes_faces[arete].append(i)
            else:
                aretes_faces[arete] = [i]
    bord = [arete for arete, faces in aretes_faces.items() if len(faces) == 1]
    return bord
```