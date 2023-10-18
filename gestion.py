tasks = []

def add_task(task):
    tasks.append(task)
    print("Tâche ajoutée avec succès!")

def show_tasks():
    if not tasks:
        print("Aucune tâche à afficher!")
    else:
        print("Liste des tâches :")
        for i in enumerate(tasks):
            print(f"{i[0]}. {i[1]}")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Tâche supprimée : {removed_task}")
    else:
        print("Indice de tâche invalide.")

while True:
    print("\nOptions disponibles :")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choice = input("Choisissez une option (1/2/3/4) : ")
    if choice == '1':
        task = input("Entrez la tâche : ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        task_index = int(input("Entrez l'indice de la tâche à supprimer : "))
        remove_task(task_index)
    elif choice == '4':
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")

