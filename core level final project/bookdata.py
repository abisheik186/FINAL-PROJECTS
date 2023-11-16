import valid
import random
import string
from tabulate import tabulate
class BookData:
    def __init__(self):
        #dictionary of available books with book title as key and details are as list
        self.book_dict={'pm123': ['The psychology of money','morgan housel','978-9-90166-263-8','study guide',15,3,300],
                        'bq456':['brief answers to the big questions','stephen hawkins','978-1-47369-599-3','Autobiography',20,8,250],
                        'ph789':['Project Hail Mary','andy weir','978-5-93135-220-8','sci-fi',0,3,350],
                        'ml101':['The Midnight Library','matt haig','978-3-42630-825-7','sci-fi',20,5,200]}
        self.books=['aefsss']
    def add_book(self):
        book_details=[]     #empty list for storing book details
        f=1
        while f:
            book_title=input('Enter the title of the book :')
            if valid.booktitle_valid(book_title):       #validations for book details
                for i in self.book_dict.values():
                    if book_title not in i:
                        f=2
                    else:
                        f=3
            if f==2:
                book_details.append(book_title)
                f=0
            elif f==3:
                print('Entered book is already given')
        while True:
            author=input('Enter the author of the book :')
            if valid.name_validation(author):
                break
        book_details.append(author)
        f=1
        while f:
            isbn=input('Enter the ISBN of the book(978-1-23456-789-0) :')
            if valid.isbn(isbn):
                for i in self.book_dict.values():
                    if isbn not in i:
                        f=2
                    else:
                        f=3
            if f==2:
                book_details.append(isbn)
                f=0
            elif f==3:
                print('Entered isbn is already given')
        while True:
            genre=input('Enter the genre of the book :')
            if valid.genre_validation(genre):
                break
        book_details.append(genre)
        while True:
            avail_copies=input('Enter the number of copies available :')
            if valid.no_copies(avail_copies):
                break
        book_details.append(int(avail_copies))
        book_details.append(0)
        while True:
            book_cost=input('Enter the cost of the book :')
            if valid.book_cost_valid(book_cost):
                break
        book_details.append(book_cost)
        stt = ''.join(random.choices(book_title,k=2))
        digit=''.join(random.choices(string.digits, k=3))
        book_id=stt+digit
        self.book_dict[book_id]=book_details     #storing book details list into dictionary by having book title as key
        print('Book added successfully.')
        print(f'added book id is {book_id}')
    def update_book(self):
        while True:
            while True:
                u_bookid=input('Enter the book id of the book :')
                if valid.bookid_valid(u_bookid):
                    break
            while True:
                u_isbn=input('Enter the ISBN of the book :')
                if valid.isbn(u_isbn):
                    break
            if u_bookid in self.book_dict:
                if self.book_dict[u_bookid][2]==u_isbn:
                    print('list of member details\n'+'='*20,'\n1.Book name \n2.Book Author \n3.Book genre\n4.Available copies of book\n5.cost of the book')
                    print('what do you want to update?')
                    ch=input('pick a choice :')
                    if ch=='1':
                        while True:
                            name=input('Enter New Title :')
                            if valid.booktitle_valid(name):
                                break
                        self.book_dict[u_bookid][0]=name
                    elif ch=='2':
                        while True:
                            author=input('Enter author name to update :')
                            if valid.name_validation(author):
                                break
                            self.book_dict[u_bookid][1]=author
                    elif ch=='3':
                        while True:
                            genre=input('Enter genre name to update :')
                            if valid.genre_validation(genre):
                                break
                            self.book_dict[u_bookid][3]=genre
                    elif ch=='4':
                        while True:
                            avail_copies=input('Enter new number of copies :')
                            if valid.no_copies(avail_copies):
                                break
                            self.book_dict[u_bookid][4]=int(avail_copies)
                    elif ch=='5':
                        while True:
                            cost=input('Enter new cost of the book :')
                            if valid.book_cost_valid(cost):
                                break
                            self.book_dict[u_bookid][6]=int(cost)
                    else:
                        print('please enter valid choice')
                    break
                else:
                    print('book title and ISBN is mismatching please enter correct ISBN')
            else:
                print('entered book is not available')
        print('Book updated successfully.')
                                                                                    #printing added book information by slicing the stored list in dictionary
        print("Title :{}(Updated)\nAuthor :{}\nISBN :{}\nGenre :{}\
                \nNumber of Copies Available :{}\nNumber of Copies Borrowed :{}".format(self.book_dict[u_bookid][0],self.book_dict[u_bookid][1],self.book_dict[u_bookid][2],self.book_dict[u_bookid][3],self.book_dict[u_bookid][4],self.book_dict[u_bookid][5]))
    def delete_book(self):
        while True:
            d_bookid=input('Enter the book id of the book :')
            if valid.bookid_valid(d_bookid):
                break
        while True:
            d_isbn=input('ISBN :')
            if valid.isbn(d_isbn):
                break
        if d_bookid in self.book_dict:       #checking if the given book title is available in the all book dictionary
            if self.book_dict[d_bookid][2]==d_isbn:      #checking whether the given isbn number is associated with the given book title
                
                print("Title :{}\nAuthor :{}\nISBN :{}\nGenre :{}\
                        \nNumber of Copies Available :{}\nNumber of Copies Borrowed :{}".format(self.book_dict[d_bookid][0],self.book_dict[d_bookid][1],self.book_dict[d_bookid][2],self.book_dict[d_bookid][3],self.book_dict[d_bookid][4],self.book_dict[d_bookid][5]))
                while True:
                    ch=input('Do you want to delete this book(y/n) :').lower()
                    if ch=='y':
                        del(self.book_dict[d_bookid])
                        print('Book deleted successfully')
                        break
                    elif ch=='n':
                        print('Book not deleted ')
                        break
                    else:
                        print('please enter choice between y and n.')
            else:
                print('book title and ISBN is mismatching please enter correct ISBN')
        else:
            print('entered book is not available')
    def search_book(self):
        while True:
            d_bookid=input('Enter the book id of the book :')
            if valid.bookid_valid(d_bookid):
                break
        if d_bookid in self.book_dict:       #printing added book information by slicing the stored list in dictionary
            print(tabulate([self.book_dict[d_bookid]],headers=['Title','Author','ISBN','Genre','available copies','borrowed copies'],tablefmt='grid',stralign='center'))
        else:
            print('Entered book is not available')
