def ExtraireBord(M):
    # M est un tuple (sommets, arêtes)
    sommets, aretes = M
    bord = set()
    for arete in aretes:
        # Crée une arête entre chaque paire de sommets consécutifs dans la face
        arete = tuple(sorted((arete[0], arete[1])))
        if arete in bord:
            # Si l'arête est déjà dans le bord, elle est partagée par deux faces
            # et n'est donc pas une arête de bord
            bord.remove(arete)
        else:
            # Sinon, ajoute l'arête au bord
            bord.add(arete)
    return bord