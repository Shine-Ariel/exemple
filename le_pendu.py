import tkinter as tk
from tkinter import messagebox
import random

# Liste des mots
mots = ["moi", "avril", "imbecile"]

# Initialisation
mot_a_deviner = random.choice(mots)
lettres = []
possibilitees = 7

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Le jeu du pendu")

# Fonction pour vérifier si le jeu est terminé
def fin_du_jeu():
    return victoire() or game_over()

# Vérifie si toutes les lettres ont été trouvées
def victoire():
    return all(lettre in lettres for lettre in mot_a_deviner)

# Vérifie si le joueur a perdu
def game_over():
    return possibilitees == 0

# Gestion des entrées de lettres
def verifier_lettre():
    global possibilitees
    lettre = lettre_entree.get().lower()
    if lettre.isalpha() and len(lettre) == 1:
        if lettre in lettres:
            messagebox.showinfo("Information", f"Vous avez déjà essayé '{lettre}'")
        elif lettre in mot_a_deviner:
            lettres.append(lettre)
            update_mot_display()
            if victoire():
                messagebox.showinfo("Victoire", "Félicitations, vous avez gagné !")
                reset_game()
        else:
            lettres.append(lettre)
            possibilitees -= 1
            update_possibilitees_display()
            draw_pendu()
            if game_over():
                messagebox.showinfo("Défaite", f"Vous avez perdu ! Le mot était : {mot_a_deviner}")
                reset_game()
        lettre_entree.delete(0, tk.END)
    else:
        messagebox.showinfo("Erreur", "Veuillez entrer une seule lettre.")

# Réinitialise le jeu
def reset_game():
    global mot_a_deviner, lettres, possibilitees
    mot_a_deviner = random.choice(mots)
    lettres.clear()
    possibilitees = 6
    update_mot_display()
    update_possibilitees_display()
    canvas.delete("pendu")
    draw_pendu()

# Met à jour l'affichage du mot
def update_mot_display():
    display_mot = ""
    for lettre in mot_a_deviner:
        if lettre in lettres:
            display_mot += lettre
        else:
            display_mot += "_"
        display_mot += " "
    mot_label.config(text=display_mot.strip())

# Met à jour l'affichage des possibilités restantes
def update_possibilitees_display():
    possibilitees_label.config(text=f"Il vous reste {possibilitees} possibilité(s)")

# Dessine le pendu en fonction des erreurs
def draw_pendu():
    canvas.delete("pendu")
    if possibilitees < 7:
        canvas.create_line(150, 50, 150, 75, width=4, tags="pendu")  # Tête
    if possibilitees < 6:
        canvas.create_oval(125, 50, 175, 100, width=4, tags="pendu")  # Tête
    if possibilitees < 5:
        canvas.create_line(150, 100, 150, 175, width=4, tags="pendu")  # Corps
    if possibilitees < 4:
        canvas.create_line(150, 125, 125, 150, width=4, tags="pendu")  # Bras gauche
    if possibilitees < 3:
        canvas.create_line(150, 125, 175, 150, width=4, tags="pendu")  # Bras droit
    if possibilitees < 2:
        canvas.create_line(150, 175, 125, 225, width=4, tags="pendu")  # Jambe gauche
    if possibilitees < 1:
        canvas.create_line(150, 175, 175, 225, width=4, tags="pendu")  # Jambe droite

# Widgets
mot_label = tk.Label(fenetre, text="", font=("Arial", 24))
possibilitees_label = tk.Label(fenetre, text="", font=("Arial", 16))
lettre_entree = tk.Entry(fenetre, width=5, font=("Arial", 16))
bouton_devine = tk.Button(fenetre, text="Devine", command=verifier_lettre)
bouton_reset = tk.Button(fenetre, text="Reset", command=reset_game)
canvas = tk.Canvas(fenetre, width=300, height=300)
canvas.create_line(50, 250, 250, 250, width=4)  # Base
canvas.create_line(200, 250, 200, 50, width=4)  # Poteau
canvas.create_line(100, 50, 200, 50, width=4)  # Traverse

# Placement des widgets
mot_label.pack(pady=10)
possibilitees_label.pack(pady=10)
lettre_entree.pack(pady=10)
bouton_devine.pack(pady=10)
bouton_reset.pack(pady=10)
canvas.pack()

# Initialisation
update_mot_display()
update_possibilitees_display()
draw_pendu()

# Lancement du jeu
fenetre.mainloop()
