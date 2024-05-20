import tkinter as tk
import ex1
import ex2
import ex3
import polyscope as ps

def run_ex1():
    print("Exercice 1")
    ex1.main()

def run_ex2():
    print("Exercice 2")
    ps.init()
    cube, vertices, edges = ex1.mesh_cube()
    ex2.ExtraireBord((vertices, edges))
    ps.show()
    

def run_ex3():
    print("Exercice 3")
    ps.init()
    cube, vertices, edges = ex1.mesh_cube()
    oriantedVertices, orientedEdges = ex3.OrienterMaillage((vertices, edges))
    ps.register_surface_mesh("EX3"+ex1.random_name(), oriantedVertices, orientedEdges)
    ps.show()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")  # Définir la taille de la fenêtre à 800x600

    frame = tk.Frame(root)
    frame.pack(expand=True)

    ex1_button = tk.Button(frame, text="Exercice 1", command=run_ex1)
    ex1_button.pack(fill=tk.X, ipadx=50, ipady=20)  # Agrandir et centrer le bouton
    ex2_button = tk.Button(frame, text="Exercice 2", command=run_ex2)
    ex2_button.pack(fill=tk.X, ipadx=50, ipady=20)  # Agrandir et centrer le bouton
    ex3_button = tk.Button(frame, text="Exercice 3", command=run_ex3)
    ex3_button.pack(fill=tk.X, ipadx=50, ipady=20)  # Agrandir et centrer le bouton

    root.mainloop()