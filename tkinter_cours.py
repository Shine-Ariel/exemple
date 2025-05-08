import tkinter as tk  # Importation de Tkinter pour l'interface graphique
from tkinter import messagebox  # Importation de messagebox pour afficher des alertes
import sqlite3  # Importation de sqlite3 pour gérer la base de données SQLite

# Connexion à la base de données SQLite (création du fichier si non existant)
conn = sqlite3.connect("todo.db")  # Création et connexion à la base de données "todo.db"
cursor = conn.cursor()  # Création d'un curseur pour exécuter des requêtes SQL

# Création de la table si elle n'existe pas encore
cursor.execute("""
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID unique auto-incrémenté
        nom TEXT NOT NULL,  -- Nom de la tâche (obligatoire)
        priorite TEXT DEFAULT '',  -- Priorité (haute, moyenne, basse)
        echeance TEXT DEFAULT '',  -- Date d'échéance au format jj/mm/aaaa
        description TEXT DEFAULT ''  -- Description de la tâche
    )
""")
conn.commit()  # Validation des modifications

# Dictionnaire pour stocker temporairement les détails des tâches chargées depuis la base
details_dict = {}

def charger_taches():
    """Charge toutes les tâches enregistrées dans la base de données et met à jour l'affichage."""
    details_dict.clear()  # Réinitialisation du dictionnaire pour éviter des doublons
    cursor.execute("SELECT * FROM taches")  # Récupération des tâches
    for row in cursor.fetchall():
        # Stockage des détails de chaque tâche dans un dictionnaire
        details_dict[row[1]] = {"id": row[0], "priorite": row[2], "echeance": row[3], "description": row[4]}
    mettre_a_jour_affichage()  # Rafraîchissement de l'affichage

def ajouter_la_tache():
    """Ajoute une nouvelle tâche à la base de données."""
    tache = tache_entree.get().strip()  # Récupération du texte saisi sans espaces inutiles
    if tache:
        cursor.execute("INSERT INTO taches (nom) VALUES (?)", (tache,))  # Ajout à la base
        conn.commit()
        charger_taches()  # Rafraîchissement de la liste
        tache_entree.delete(0, tk.END)  # Effacement du champ d'entrée après l'ajout
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche.")  # Alerte si champ vide

def supprimer_la_tache():
    """Supprime une tâche sélectionnée de la base de données."""
    index_selectionne = tache_listbox.curselection()  # Vérification de la sélection
    if index_selectionne:
        tache = tache_listbox.get(index_selectionne[0]).split(". ", 1)[1]  # Extraction du nom de la tâche
        tache_id = details_dict[tache]["id"]  # Récupération de l'ID
        cursor.execute("DELETE FROM taches WHERE id=?", (tache_id,))  # Suppression dans la base
        conn.commit()
        charger_taches()  # Rafraîchissement de la liste
        details_des_taches.delete("1.0", tk.END)  # Effacement de la zone de détails
    else:
        messagebox.showwarning("Attention", "Aucune tâche sélectionnée!")  # Alerte si aucune sélection

def afficher_les_details(event):
    """Affiche les détails d'une tâche sélectionnée dans la zone de texte."""
    index_selectionne = tache_listbox.curselection()
    if index_selectionne:
        tache = tache_listbox.get(index_selectionne[0]).split(". ", 1)[1]  # Extraction du nom de la tâche
        details = details_dict.get(tache, {})  # Récupération des détails
        details_text = (f"Priorité: {details.get('priorite', 'Non définie')}\n"
                        f"Échéance: {details.get('echeance', 'Non définie')}\n"
                        f"Description: {details.get('description', 'Aucune')}")
        details_des_taches.delete("1.0", tk.END)  # Effacement du texte précédent
        details_des_taches.insert(tk.END, details_text)  # Affichage des détails

def ouvrir_fenetre_details(event):
    """Ouvre une fenêtre pour modifier les détails d'une tâche sélectionnée."""
    global fenetre_details, entree_priorite, entree_echeance, entree_description, tache_actuelle

    index_selectionne = tache_listbox.curselection()
    if not index_selectionne:
        messagebox.showwarning("Attention", "Aucune tâche sélectionnée!")
        return
    try:
        index_selectionne = tache_listbox.curselection()[0]
        tache_actuelle = tache_listbox.get(index_selectionne).split(". ", 1)[1]
        details = details_dict.get(tache_actuelle, {})

        fenetre_details = tk.Toplevel(fenetre)
        fenetre_details.title("Ajouter des détails")
        fenetre_details.geometry("300x200")
        fenetre_details.resizable(False, False)  # Fenêtre fixe

        tk.Label(fenetre_details, text="Priorité (haute/moyenne/basse):").pack()
        entree_priorite = tk.Entry(fenetre_details, width=40)
        entree_priorite.pack(pady=2)
        entree_priorite.insert(0, details.get("priorite", ""))

        tk.Label(fenetre_details, text="Date d'échéance (jj/mm/aaaa):").pack()
        entree_echeance = tk.Entry(fenetre_details, width=40)
        entree_echeance.pack(pady=2)
        entree_echeance.insert(0, details.get("echeance", ""))

        tk.Label(fenetre_details, text="Description:").pack()
        entree_description = tk.Entry(fenetre_details, width=40)
        entree_description.pack(pady=2)
        entree_description.insert(0, details.get("description", ""))

        bouton_valider = tk.Button(fenetre_details, text="Ajouter", command=ajouter_details)
        bouton_valider.pack(pady=5)
    except IndexError:
        messagebox.showwarning("Attention", "Aucune tâche sélectionnée!")

def ajouter_details():
    """Ajoute ou modifie les détails d'une tâche en convertissant les entrées en minuscules."""
    global tache_actuelle
    if tache_actuelle in details_dict:
        details_dict[tache_actuelle] = {
            "priorite": entree_priorite.get().strip().lower(),
            "echeance": entree_echeance.get().strip().lower(),
            "description": entree_description.get().strip()
        }
    fenetre_details.destroy()
    mettre_a_jour_affichage()

def modifier_details():
    """Modifie les détails d'une tâche dans la base de données."""
    global tache_actuelle
    if tache_actuelle in details_dict:
        tache_id = details_dict[tache_actuelle]["id"]
        cursor.execute("""
            UPDATE taches 
            SET priorite=?, echeance=?, description=? 
            WHERE id=?
        """, (entree_priorite.get().strip().lower(),
              entree_echeance.get().strip(),
              entree_description.get().strip(),
              tache_id))
        conn.commit()
    fenetre_details.destroy()
    charger_taches()

def mettre_a_jour_affichage():
    """Met à jour la liste des tâches en les triant par priorité."""
    tache_listbox.delete(0, tk.END)
    priorites = {"haute": [], "moyenne": [], "basse": [], "": []}
    for tache, info in details_dict.items():
        priorites[info["priorite"]].append(tache)
    taches_triees = priorites["haute"] + priorites["moyenne"] + priorites["basse"] + priorites[""]

    for index, tache in enumerate(taches_triees, start=1):
        tache_listbox.insert(tk.END, f"{index}. {tache}")
        couleur = "black"
        if details_dict[tache]["priorite"] == "haute":
            couleur = "red"
        elif details_dict[tache]["priorite"] == "moyenne":
            couleur = "orange"
        elif details_dict[tache]["priorite"] == "basse":
            couleur = "green"
        tache_listbox.itemconfig(index - 1, fg=couleur)

def fermer_application():
    """Ferme l'application proprement."""
    conn.close()
    fenetre.destroy()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("ToDo List")
fenetre.geometry("500x450")
fenetre.configure(bg="orange")
fenetre.protocol("WM_DELETE_WINDOW", fermer_application)

# Cadre pour centrer les éléments
cadre = tk.Frame(fenetre, bg="orange")
cadre.pack(expand=True)

# Champ d'entrée pour ajouter des tâches
tache_entree = tk.Entry(cadre, width=30)
tache_entree.pack(pady=10)

# Bouton pour ajouter une tâche
bouton_ajouter = tk.Button(cadre, text="Ajouter", command=ajouter_la_tache, bg="green", fg="white")
bouton_ajouter.pack()

# Liste des tâches
tache_listbox = tk.Listbox(cadre, width=40, height=10)
tache_listbox.pack(pady=10)
tache_listbox.bind("<<ListboxSelect>>", afficher_les_details)
tache_listbox.bind("<Double-Button-1>", ouvrir_fenetre_details)

# Bouton pour supprimer une tâche
bouton_supprimer = tk.Button(cadre, text="Supprimer", command=supprimer_la_tache, bg="red", fg="white")
bouton_supprimer.pack()

# Zone de texte pour afficher les détails
details_des_taches = tk.Text(cadre, width=35, height=5)
details_des_taches.pack(pady=10)

# Chargement des tâches existantes au démarrage
charger_taches()

# Lancement de la boucle principale Tkinter
fenetre.mainloop()