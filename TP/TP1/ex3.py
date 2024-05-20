import numpy as np

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