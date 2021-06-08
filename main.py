def menu():
    print
    switcher ={
        0: "Quitter le programme",
        1: "Afficher les coureurs",
        2: "Afficher le classement provisoire",
        3: "Enregistrer une arrivée",
        4: "Enregistrer un abandon",
        5: "Enregistrer une disqualification",
        6: "Enregistrer le temps d'arrivée d'un coureur",
        7: "Obtenir le temps d'un coureur",
        8: "Obtenir l'écart de temps entre 2 coureurs donnés",
    }
    return switcher.get("Choix invalide")
print(menu())