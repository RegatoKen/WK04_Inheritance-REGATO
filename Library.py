class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn) 
        self.file_size = file_size

    def display_details(self):
        return f"Ebook - {super().display_details()}, File Size: {self.file_size} MB"

class PrintedBook(Book):
    def __init__(self, title, author, isbn, num_pages):
        super().__init__(title, author, isbn)
        self.num_pages = num_pages

    def display_details(self):
        return f"Printed Book - {super().display_details()}, Number of Pages: {self.num_pages}"
if __name__ == "__main__":
    ebook1 = Ebook("Filipino Children's Favorite Stories", "Liana Romulo", "978-1462908011", 56)
    ebook2 = Ebook("The First Filipino", "Liana Romulo", "978-1623092931", 1)
    ebook3 = Ebook("Pagkatuklas sa ating Lupain", "Sofronio G. Calderon", "978-1141091492", 5.77)
    ebook4 = Ebook("The Filipino Heroes League: Book One: Sticks and Stones", "Paolo Fabregas", " 978-9712727940", 62.7)
    ebook5 = Ebook("My First Book of Tagalog Words: Filipino Rhymes and Verses", "Cora Salvacion Castle", "978-1444105674", 12)

    printed_book1 = PrintedBook("Filipino Popular Tales", " Dean S. Fansler", "978-0559950049", 496)
    printed_book2 = PrintedBook("Jose Rizal: The Filipino Hero's Life Illustrated", "Takahiro Matsui", " 978-9712735257", 111)
    printed_book3 = PrintedBook("The Alchemist", "Paulo Coelho", "978-0062315007", 208)
    printed_book4 = PrintedBook("War and Peace", "Leo Tolstoy", "978-1400079988", 1296)
    printed_book5 = PrintedBook("Crime and Punishment", "Fyodor Dostoevsky", "978-0486415871", 430)

    print("\nEBooks\n")
    print(ebook1.display_details())
    print(ebook2.display_details())
    print(ebook3.display_details())
    print(ebook4.display_details())
    print(ebook5.display_details())

    print("\nPrinted Books\n")
    print(printed_book1.display_details())
    print(printed_book2.display_details())
    print(printed_book3.display_details())
    print(printed_book4.display_details())
    print(printed_book5.display_details())  