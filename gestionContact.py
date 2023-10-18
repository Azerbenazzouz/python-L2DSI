contacts = []
def add_contact(name, email, phone):
    contact = {"Nom": name, "Email": email, "Téléphone": phone}
    contacts.append(contact)
    print("Contact ajouté avec succès!")

def show_contacts():
    if not contacts:
        print("Aucun contact à afficher.")
    else:
        print("Liste des contacts :")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['Nom']} - Email : {contact['Email']} -Téléphone : {contact['Téléphone']}")

def search_contact(name):
    matching_contacts = [contact for contact in contacts if contact["Nom"].lower() == name.lower()]
    if matching_contacts:
        print("Résultats de la recherche :")
        for contact in matching_contacts:
            print(f"Nom : {contact['Nom']} - Email : {contact['Email']} -Téléphone : {contact['Téléphone']}")
    else:
        print(f"Aucun contact trouvé avec le nom '{name}'.")

def remove_contact(name):
    matching_contacts = [contact for contact in contacts if
    contact["Nom"].lower() == name.lower()]
    if matching_contacts:
        for contact in matching_contacts:
            contacts.remove(contact)
            print(f"Contact '{contact['Nom']}' supprimé avec succès.")
    else:
        print(f"Aucun contact trouvé avec le nom '{name}'.")

while True:
    print("\nOptions disponibles :")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Rechercher un contact par nom")
    print("4. Supprimer un contact par nom")
    print("5. Quitter")
    choice = input("Choisissez une option (1/2/3/4/5) : ")
    if choice == '1':
        name = input("Nom du contact : ")
        email = input("Email du contact : ")
        phone = input("Téléphone du contact : ")
        add_contact(name, email, phone)
    elif choice == '2':
        show_contacts()
    elif choice == '3':
        name = input("Entrez le nom à rechercher : ")
        search_contact(name)
    elif choice == '4':
        name = input("Entrez le nom du contact à supprimer : ")
        remove_contact(name)
    elif choice == '5':
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")