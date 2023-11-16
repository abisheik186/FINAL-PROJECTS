import valid
import bookdata
import memberdata
import borrowingsystem
import datetime
from tabulate import tabulate
class Reporting_System(borrowingsystem.Borrowing_System):
    def book_availability(self):
        tab=[]
        for i,j in self.book_dict.items():
            avail='available' if j[4]>0 else 'not available'    #checking whether the book is available or not available
            j.append(avail) #appending into the list of book values
        while True:
            genre=input('Enter genre :')
            if valid.genre_validation(genre):
                break
        for i,j in self.book_dict.items():
            if genre==j[3]:
                lis=[j[0],j[1],j[2],j[6]]   #storing all the name,author,isbn,and availability into the lis list
                tab.append(lis) #appending the list into tab empty list to use in the tabulate function
        headers=['Title','Author','ISBN','Availability']
        print(tabulate(tab,headers=headers,tablefmt='grid',stralign='center'))
    def borrowing_history(self):
        bor_his=[]
        if not len(self.member_dict)==0:
            bh_mem_id=input('Member ID :')
            if bh_mem_id in self.member_dict:
                print(f'\nName :{self.member_dict[bh_mem_id][0]}\nAddress :{self.member_dict[bh_mem_id][1]}\
                        \nPhone Number :{self.member_dict[bh_mem_id][2]}\nEmail Address :{self.member_dict[bh_mem_id][3]}')
                print('Borrowing History:')
                print(tabulate(self.member_dict[bh_mem_id][6],headers=['Title','Author','ISBN','Date Borrowed','Due Date'],tablefmt='grid',stralign='center'))
            else:
                print('Youre not registered. please enter valid member id')
        else:
            print('nobody has registered')
    def overdue_report(self):
        date_format='%Y-%m-%d'
        while True:
            try:
                ov_date=input('Enter date to check overdue :')
                date = datetime.datetime.strptime(ov_date, date_format).date()#converting string date input into date object
                break
            except ValueError:
                print('Incorrect date format.date format is yyyy-mm-dd')
        f=0
        for i,j in self.member_dict.items():
            for k in j[6]:
                if date>k[4]:   #comparing the date with due date
                    overdue=j[5]
                else:
                    f=1
        if f==0:
            print(tabulate(overdue,headers=['Title','Author','ISBN','Date Borrowed','Due Date'],tablefmt='grid'))
        elif f==1:
            print('There are no overdue books')
    def show_all_available_books(self):
        print(tabulate(self.book_dict.values(),headers=['Book title','Book author','ISBN','genre','availabiity','borrowed','price'],tablefmt='grid'))
s1=Reporting_System()
