from Book import Book
from Member import Member

class Library(Book, Member):

    def __init__(self):
        self.booklist = []
        self.memberlist = []
        self.issuelist = []
        
    def listAllBooks(self):
        print("\n-------- Printing all books ---------")
        fh = open('./bookdata.csv','r')
        for line in fh.readlines():
            print(line)
        fh.close()
        print("------------------------------------\n")

    def listAllMemberships(self):
        print("-------- Printing all memberships ---------")
        fh = open('./memberdata.csv','r')
        for line in fh.readlines():
            print(line)
        fh.close()
        print("------------------------------------")
    
    def listAllBooksForGenre(self, genre):
        genreStr = str(genre)
        print("Searching books for genre '" + genre + "'... ")
        fh = open('./bookdata.csv','r')
        for line in fh.readlines():
            columns = line.split(",")
            if (genreStr.lower() == columns[4].lower()):
                print(columns[1])
        fh.close()
        print("------------------------------------")