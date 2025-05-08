import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Création de la table si elle n'existe pas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        priorite TEXT CHECK(priorite IN ('haute', 'moyenne', 'basse', '')) DEFAULT '',
        echeance TEXT DEFAULT '',
        description TEXT DEFAULT ''
    )
""")
conn.commit()

details_dict = {}


def charger_taches():
    """Charge et affiche toutes les tâches triées par priorité."""
    details_dict.clear()
    cursor.execute(
        "SELECT * FROM taches ORDER BY CASE priorite WHEN 'haute' THEN 1 WHEN 'moyenne' THEN 2 WHEN 'basse' THEN 3 ELSE 4 END")
    tache_listbox.delete(0, tk.END)

    for index, row in enumerate(cursor.fetchall(), start=1):
        details_dict[row[1]] = {"id": row[0], "priorite": row[2], "echeance": row[3], "description": row[4]}
        couleur = {"haute": "red", "moyenne": "orange", "basse": "green"}.get(row[2], "black")
        tache_listbox.insert(tk.END, f"{index}. {row[1]}")
        tache_listbox.itemconfig(index - 1, fg=couleur)


def ajouter_la_tache():
    """Ajoute une tâche si le champ est rempli."""
    tache = tache_entree.get().strip()
    if tache:
        cursor.execute("INSERT INTO taches (nom) VALUES (?)", (tache,))
        conn.commit()
        charger_taches()
        tache_entree.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche.")


def supprimer_la_tache():
    """Supprime la tâche sélectionnée après confirmation."""
    index_selectionne = tache_listbox.curselection()
    if index_selectionne:
        tache = tache_listbox.get(index_selectionne[0]).split(". ", 1)[1]
        if messagebox.askyesno("Confirmation", f"Supprimer '{tache}' ?"):
            cursor.execute("DELETE FROM taches WHERE id=?", (details_dict[tache]["id"],))
            conn.commit()
            charger_taches()
            details_des_taches.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Attention", "Aucune tâche sélectionnée!")


def afficher_les_details(event):
    """Affiche les détails d'une tâche sélectionnée."""
    index_selectionne = tache_listbox.curselection()
    if index_selectionne:
        tache = tache_listbox.get(index_selectionne[0]).split(". ", 1)[1]
        details = details_dict.get(tache, {})
        details_des_taches.delete("1.0", tk.END)
        details_des_taches.insert(tk.END,
                                  f"Priorité: {details.get('priorite', 'Non définie')}\nÉchéance: {details.get('echeance', 'Non définie')}\nDescription: {details.get('description', 'Aucune')}")


def fermer_application():
    """Ferme l'application en fermant la connexion."""
    conn.close()
    fenetre.destroy()


# Interface graphique
fenetre = tk.Tk()
fenetre.title("ToDo List")
fenetre.geometry("500x450")
fenetre.configure(bg="orange")
fenetre.protocol("WM_DELETE_WINDOW", fermer_application)

cadre = tk.Frame(fenetre, bg="orange")
cadre.pack(expand=True)

tache_entree = tk.Entry(cadre, width=30)
tache_entree.pack(pady=10)

bouton_ajouter = tk.Button(cadre, text="Ajouter", command=ajouter_la_tache, bg="green", fg="white")
bouton_ajouter.pack()

tache_listbox = tk.Listbox(cadre, width=40, height=10)
tache_listbox.pack(pady=10)
tache_listbox.bind("<<ListboxSelect>>", afficher_les_details)

bouton_supprimer = tk.Button(cadre, text="Supprimer", command=supprimer_la_tache, bg="red", fg="white")
bouton_supprimer.pack()

details_des_taches = tk.Text(cadre, width=35, height=5)
details_des_taches.pack(pady=10)

charger_taches()
fenetre.mainloop()
