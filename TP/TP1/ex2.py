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