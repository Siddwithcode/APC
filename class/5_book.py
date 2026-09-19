class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"[{self.book_id}] {self.title} by {self.author} - ${self.price}")

b1 = Book(1, "1984", "George Orwell", 15)
b2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 12)
b3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald", 10)

b1.display_info()
b2.display_info()
b3.display_info()
