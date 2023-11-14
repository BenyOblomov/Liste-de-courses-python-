LISTE = []
MENU = ("Choisissez parmi les 5 options suivantes :\n1: Ajouter un élément à la liste\n2: Retirer un élément de la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter")
choice = []
while choice != "5" :
    print("-" * 50)
    print(MENU)
    choice = input("👉   Votre choix : ")
    if choice == "1" :
        element_to_add = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(element_to_add)
        print(f"L'élément {element_to_add} a bien été ajouté à la liste.")
    if choice == "3" :
        if LISTE == [] :
            print("Votre liste ne contient aucun élément.")
        else :
            print("Voici le contenu de votre liste :")
            for index, value in enumerate(LISTE) :
                print(f"{index + 1}: {value}")
    if choice == "2" :
        element_to_delete = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if element_to_delete in LISTE :
            print(f"L'élément {element_to_delete} a bien été supprimé de la liste.")
            LISTE.remove(element_to_delete)
        else :
            print(f"L'élément {element_to_delete} n'est pas dans la liste.")
    if choice == "4" :
        LISTE.clear()
        print("La liste a bien été vidée de son contenu.")
    if choice == "5" :
        print("A bientôt !")