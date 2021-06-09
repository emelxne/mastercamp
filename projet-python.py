choix = 100
list2D = [["javier", "benoit", "christian", "bertrand"], ["NON", "NON", "NON", "NON"], ["NON", "NON", "NON", "NON"], [1.00, 1.55 , 1.56, 2.53]]
print("0.Quitterle programme")
print("1.Afficherlescoureurs")
print("2.Afficherleclassementprovisoire")
print("3.Enregistrerunearrivée")
print("4.Enregistrerunabandon")
print("5.Enregistrerunedisqualification")
print("6.Enregistrerletemps d’arrivée d’un coureur")
print("7.Obtenirletemps d’un coureur")
print("8.Obtenir l’écart de temps entre deux coureursdonnés")
while choix != 255:
    choix = int(input("saisi la valeur numerique correspondant a l'action désiré:"))
    if choix == 0:
        print("Fin du programme aurevoir!")
        choix = 255
    elif choix == 1:
        for i in range(0, len(list1D)):
            print(list1D[i])
    elif choix == 2:
        for i in range(0, len(list2D[0])):
            print("POS#", i+1, "coureur:", list2D[0][i])
            # for i in range(0, len(list2D[0])):
            # print(list2D[0][i])
    elif choix == 3:
        list2D[0].append(input("saisi le coureur qui vient d'arriver: "))
        for i in range(0, len(list2D[0])):
            print(list2D[0][i])
    elif choix == 4:
        list2D[1].insert(int(input("saisi le numéro de dossard du coureur pour indiquer si il a abbandoner")), input("saisi si \"OUI\" ou \"NON\""))
        for i in range(0, len(list2D[1])):
            print(list2D[1][i])
    elif choix == 5:
        list2D[2].insert(int(input("saisi le numéro de dossard du coureur pour indiquer une disqualification")), input("saisi si \"OUI\" ou \"NON\""))
        for i in range(0, len(list2D[2])):
            print(list2D[2][i])
    elif choix == 6:
        list2D[3].insert(int(input("saisi le numéro de dossard du coureur pour indiquer son chrono")), float(input("donner le temps en minute")))
        for i in range(0, len(list2D[3])):
            print(list2D[3][i])
    elif choix == 7:
        i=int(input("saisi le numéro de dossard du coureur pour obtenir son chrono"))
        print("le coureur: ", list2D[0][i], "à réalisé un chrono de :", list2D[3][i], "en minute")
    elif choix == 8:
        i = int(input("saisi le numéro de dossard du coureur n° 1 :"))
        j = int(input("saisi le numéro de dossard du coureur n° 2 :"))
        print("la difference de chrono entre : ", list2D[0][i], "et :", list2D[0][j], "est de :", list2D[3][i]-list2D[3][j], "en minute")





