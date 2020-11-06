dic1  = {}
class Library:
  def __init__(self,name,books=list):
    self.name = name
    self.books = books
  def add_book(self):
    name = input("Enter the book : ")
    self.books.append(name)
  def lend_book(self):
    name = input("Enter your name : ")
    book = input("Enter the book : ")
    dic1[name]=book
    if book in dic1:
      print(f"The book is taken by {dic1[name]}")
    self.books.remove(book)
  def viewlist(self):
    print(self.books)
  def return_book(self):
    n = input("Enter the book :")
    self.books.append(n)
