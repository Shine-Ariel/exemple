taches = {}

def ajouter_une_tache(tache, descriptif, priorite):
    if tache not in taches:
        taches[tache] = {"Descriptif": descriptif, "Priorité": priorite}
    print(taches)

ajouter_une_tache("cash power", "payer le forfait", "urgent")
ajouter_une_tache("canal box", "réparer la box", "urgent")

def retirer_une_tache(tache, descriptif):
    if  taches[tache]["Descriptif"] == descriptif:
        del taches[tache]
    print(taches)

retirer_une_tache("cash power", "payer le forfait")
