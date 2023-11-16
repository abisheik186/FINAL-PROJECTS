import valid
import bookdata
import memberdata
import datetime
class Borrowing_System(memberdata.Member_data):
    def __init__(self):
        super().__init__()
        self.borrowed_dates={'978-5-93135-220-8':[datetime.date(2023, 7, 26),datetime.date(2023, 7, 22),datetime.date(2023, 8, 17)]}
    def borrow_book(self):
        borr_books=[]   #empty list for storing the borrowed book details, borrowed date and due date
        f=0
        price=0
        while True:
            b_mem_id=input('Enter member ID :')
            if b_mem_id in self.member_dict:        #checking whether the given member id is available in the dictionary
                break
            else:
                print('please enter registered member ID.')
        while True:
            while True:
                b_isbn=input('Enter the book ISBN to be borrowed :')
                if valid.isbn(b_isbn):      #validation for isbn number
                    break
            for i,j in self.book_dict.items():      #itetaring through the book dictionary
                if b_isbn==j[2]:        #getting the book details of given isbn number
                    if j[4]>0:  #checking the book whther the book is available or not
                        price=j[6]*.3
                        j[4]-=1     #reducing the available copies after borrowing the book
                        j[5]+=1     #increasing the borrowed copies after borrowing the book
                        borr_books.append(j[0]) #storing the book name into the borrowed book details by slicing the list of all book dictionary list of values
                        borr_books.append(j[1]) #storing the book isbn number into the borrowed book details by slicing the list of all book dictionary list of values
                        borr_books.append(price)
                    else:
                        f=2 #using flag to break the while loop and errors
                        break
                else:
                    f=1
            if f==1:
               break
            elif f==2:
                print(f'Entered ISBN book is not available right now.the book will available on {min(self.borrowed_dates[b_isbn])}')
                break
        borr_date=datetime.datetime.today().date()      #getting today date to for borrowed date using today function in datetime module
        due_date=borr_date+datetime.timedelta(days=7)   #for due date adding the 7 days using the timedelta function in dateime module
        borr_books.append(borr_date)    #storing the borrowed date in the borrowed book details
        borr_books.append(due_date)     #storing the due date in the borrowed book details
        if b_isbn in self.borrowed_dates:
            for i,j in self.borrowed_dates.items():
                    if i==b_isbn:
                         j.append(borr_date)
        else:
            list1=[]
            list1.append(borr_date)
            self.borrowed_dates[b_isbn]=list1
        self.member_dict[b_mem_id].append(borr_books)   #storing the borrowed book details into the member id values list
        if (datetime.datetime.today().year-(self.member_dict[b_mem_id][5]).year)>60:
            print('you are eligible for 10% offer on senior citizen concession')
            price-=price*.1
        print(f'Book borrowed Successfully on {borr_date},Due Date :{due_date}')
        print(f'The deposit amount to be paid for borrow the book is Rs.{price}')
        print('Return Book on/or before Due Date.Incase of late return,you should pay fine-Rs.25/day')
    def return_book(self):
        f=0
        while True:
            r_mem_id=input('Enter Member ID :')
            if r_mem_id in self.member_dict:
                break
            else:
                print('please enter registered member ID')
        while True:
            r_isbn=input('Enter borrowed book ISBN to be returned :')
            for i,j in self.book_dict.items():
                if r_isbn==j[2]:
                    if j[5]>0:      #checking the borrowed copies whether someone borrowed or not
                        j[4]+=1   #increasing the available copies after returning the book
                        j[5]-=1   #decreasing the borrowed copies after returning the book
                    else:
                        f=2
                else:
                    f=1
            if f==1:
                break
            elif f==2:
                print('the given ISBN book is never borrowed. please enter correct ISBN number')
        date_format='%Y-%m-%d'
        while True:
            try:
                ov_date=input('Enter returning date :')       #date of returning the book
                returned_date = datetime.datetime.strptime(ov_date, date_format).date()
                break
            except ValueError:
                print('Incorrect date format.date format is yyyy-mm-dd')

        flag=0
        for i in self.member_dict[r_mem_id][6]:     #iterating through the list of borrowed books by member using the member id as key
            for j in i:
                if r_isbn==j:
                    if (i[i.index(j)+2])>=returned_date:      #(i[i.index(j)+2])
                        print('Book returned successfully on ',datetime.date.today())
                    else:
                        datedue=(i[i.index(j)+2])   #getting the given due date to calculate the fine amount
                        print('Book returned successfully on ',returned_date)
                        flag=1
                        
        if flag==1:
            print('you have to pay fine charges')
            day=(returned_date-datedue).days    #calculating the number of days delayed and converting days into int 
            print('Number of days late :',day)
            fine=day*25 #calculation for fine amount
            print(f'Overdue Fine :Rs.{fine}({day} days*Rs.25/day)')

