import json
from datetime import datetime

format_date = "%d/%m/%y"
list_tache = []

def add_tache():
    new_task ={"nom": add_name, "deadline": deadline, "statu": "En attente"}
    list_tache.append(new_task)


def affiche_tache():
    for listes in list_tache:
        print("Nom : ", listes["nom"])
        print("deadline : ", listes["deadline"])
        print("statu : ", listes["statu"])
        

def get_json_data():
    with open("taches.json", "r") as file:
        return json.load(file)
    
    
def write_json_data(dico):
    json_object = json.dumps(dico, indent=4)
    with open("taches.json", "w") as readfile:
        readfile.write(json_object)


while True:
    print("1 - Pour ajouter nouvelle tâche")
    print("2 - Pour afficher les tâches")
    print("3 - Pour Modifier le tâche")
    print("4 - Pour Quitter")
    print()
    
    choix = input("Quel est votre choix : ")
    
    while choix != "1" and choix != "2" and choix != "3" and choix != "4":
        choix = input("Choix incorrect\nQuel est votre choix : ")
        
    if choix == "1":
        add_name = input("Entrer votre nom : ")
        deadline = input("Entrer la date limite (jj/mm/aaaa) : ")
        add_tache()
        
    elif choix == "2":
       
        affiche_tache()
        print("")
            
    elif choix == "4":
        write_json_data({
            "taches" : list_tache
        })
