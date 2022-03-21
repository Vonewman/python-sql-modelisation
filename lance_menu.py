import sys
import mysql.connector
from menu_requete_sql import Menu
from liste_menu import display




choix = ''
menu = Menu.liste_menu.copy()

def lancer(menu):
    """
    Lance le Menu du programme, en prenant en entrer la liste des menus
    """
    menus_popped = []
    global copy_menus
    try:
        copy_menus = menu.copy()
        while len(copy_menus) > 0:
            display(copy_menus)
            choix = input("Choisir une operation: ")
            
            if choix.lower() == 'e':
                print("Taches deja effectuees")
                lancer(menus_popped)
                
            elif choix.lower() == 'r':
                copy_menus = Menu.liste_menu.copy()
                lancer(copy_menus)
                
            elif choix.lower() != 'q':
                try:
                    connection = mysql.connector.connect(
                        host = "localhost",
                        database = "exercice_modelisation",
                        user = "root",
                        password = "root"
                    )
                    mycursor = connection.cursor()
                    choix = int(choix)
                    popped = copy_menus.pop(int(choix) - 1)
                    menus_popped.append(popped)
                    selected = Menu.requetes_sql_correspondants.get(popped)
                    print(selected)
                    mycursor.execute(selected)
                    result = mycursor.fetchall()
                    mx = max([len(str(r)) for r in result])
                    print()
                    display(result)
                    print()
                except:
                    lancer(copy_menus)
            elif choix.lower() == 'q':
                sys.exit()
                    
            print("\n")
        print("Vous etes sortis")
    except KeyboardInterrupt:
        print()
        print("you're out ")
        exit()


lancer(menu)
