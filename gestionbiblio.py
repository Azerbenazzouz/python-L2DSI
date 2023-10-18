class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def __str__(self):
        return f"{self.title} par {self.author}"
    
class Borrower:
    def __init__(self, name):
        self.name = name
        self.books = []
    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def display_books(self):
        if not self.books:
            print("La bibliothèque est vide.")
        else:
            print("Livres disponibles :")
            for book in self.books:
                if book.available:
                    print(f"- {book}")

    def display_borrowers(self):
        if not self.borrowers:
            print("Aucun emprunteur enregistré.")
        else:
            print("Emprunteurs enregistrés :")
            for borrower in self.borrowers:
                print(f"- {borrower}")

    def lend_book(self, book, borrower):
        if book in self.books and book.available:
            book.available = False
            borrower.books.append(book)
            print(f"{book.title} a été emprunté par {borrower.name}.")
        else:
            print("Ce livre n'est pas disponible.")

    def return_book(self, book, borrower):
        if book in borrower.books:
            book.available = True
            borrower.books.remove(book)
            print(f"{book.title} a été retourné par {borrower.name}.")
        else:
            print("Ce livre n'appartient pas à cet emprunteur.")

library = Library()

book1 = Book("Harry Potter et la pierre philosophale", "J.K. Rowling")
book2 = Book("Le Seigneur des Anneaux", "J.R.R. Tolkien")
borrower1 = Borrower("Alice")
borrower2 = Borrower("Bob")

library.add_book(book1)
library.add_book(book2)
library.add_borrower(borrower1)
library.add_borrower(borrower2)


while True:
    print("\nOptions disponibles :")
    print("1. Afficher les livres disponibles")
    print("2. Afficher les emprunteurs")
    print("3. Emprunter un livre")
    print("4. Retourner un livre")
    print("5. Quitter")

    choice = input("Choisissez une option (1/2/3/4/5) : ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        library.display_borrowers()
    elif choice == '3':
        borrower_name = input("Nom de l'emprunteur : ")
        book_title = input("Titre du livre à emprunter : ")

        borrower = next((b for b in library.borrowers if b.name == borrower_name), None)
        book = next((b for b in library.books if b.title == book_title), None)
        if borrower and book:
            library.lend_book(book, borrower)
        else:
            print("Emprunteur ou livre introuvable.")
    elif choice == '4':
        borrower_name = input("Nom de l'emprunteur : ")
        book_title = input("Titre du livre à retourner : ")
        
        borrower = next((b for b in library.borrowers if b.name == borrower_name), None)
        book = next((b for b in library.books if b.title == book_title), None)
        if borrower and book:
            library.return_book(book, borrower)
        else:
            print("Emprunteur ou livre introuvable.")
    elif choice == '5':
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")