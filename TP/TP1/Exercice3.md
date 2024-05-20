# Exercice 3

1. Un maillage est dit orienté si chaque face a une orientation définie, c'est-à-dire un ordre spécifique de ses sommets. Dans une structure de données de maillage, l'orientation peut être représentée par l'ordre des sommets dans chaque face. Par exemple, si les sommets sont ordonnés dans le sens des aiguilles d'une montre, la face est orientée vers l'extérieur. Si les sommets sont ordonnés dans le sens inverse des aiguilles d'une montre, la face est orientée vers l'intérieur.

2. Voici un algorithme pour orienter un maillage manifold fermé sans bords. Cet algorithme suppose que le maillage est représenté comme une liste de sommets et une liste de faces, où chaque face est une liste d'indices dans la liste de sommets.

```
Algorithme OrienterMaillage(M)
    Entrée : M, un maillage représenté par une liste de sommets et une liste de faces
    Sortie : Le maillage M avec des faces orientées

    Pour chaque face F dans M
        Si l'orientation de F n'est pas définie
            Choisir une orientation arbitraire pour F
        Fin Si
        Pour chaque face G adjacente à F
            Si l'orientation de G n'est pas définie
                Orienter G pour qu'elle soit cohérente avec F
            Sinon Si l'orientation de G est incohérente avec F
                Retourner une erreur "Le maillage n'est pas orientable"
            Fin Si
        Fin Pour
    Fin Pour
    Retourner M
Fin Algorithme
```

```python
def OrienterMaillage(M):
    # M est un tuple (sommets, faces)
    sommets, faces = M
    orientation = [None]*len(faces)
    for i, face in enumerate(faces):
        if orientation[i] is None:
            # Choisir une orientation arbitraire pour la face
            orientation[i] = face
        for j, other_face in enumerate(faces):
            if i != j and any(v in face for v in other_face):
                # Les faces sont adjacentes
                if orientation[j] is None:
                    # Orienter l'autre face pour qu'elle soit cohérente avec la face courante
                    if other_face[0] in face:
                        orientation[j] = other_face
                    else:
                        orientation[j] = list(reversed(other_face))
                elif not np.array_equal(orientation[j], other_face) and not np.array_equal(orientation[j], list(reversed(other_face))):
                    raise ValueError("Le maillage n'est pas orientable")
    return sommets, orientation
```