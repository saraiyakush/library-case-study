import csv

class Book:
    def __init__(self, bookid, name, author, year, genre, count):
        self.bookid = bookid
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.count = count
    
    def addBook(self):
        fh = open('./bookdata.csv', 'a')
        fh.write(str(self.bookid) + "," + self.name + "," + self.author + "," + str(self.year) + "," + self.genre + "," + str(self.count) + "\n")
        fh.close()

def printBook():
    fh = open('./bookdata.csv', 'r')
    print(fh.readlines())
    fh.close()
