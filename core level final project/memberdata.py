import valid
import bookdata
import random
import datetime 
class Member_data(bookdata.BookData):
    def __init__(self):
        super().__init__()      #inheriting the book dictionary using super function
        self.book_dict
        self.member_dict={'123':['abi','rani ammayar st','9442699642','abisheikk01@gmail.com','123',datetime.date(1997, 6, 18),[['The Midnight Library','matt haig','978-3-4263-0825-7',datetime.date(2023, 7, 6),datetime.date(2023, 7, 14)],['Project Hail Mary','andy weir','978-5-93135-220-8', datetime.date(2023, 7, 7),datetime.date(2023, 7, 13)]]]}
    def add_member(self):
        member_details=[]       #empty list for storing the member details 
        f=0     #flag variable
        while True:
            name=input('Enter member name :')
            if valid.name_validation(name):     #validations for member details
                break
        member_details.append(name)     #storing name in member_details list
        while True:
            address=input('Enter member address :')
            if len(address)>0:
                break
            else:
                print('address should not be empty')
        member_details.append(address)
        f=1
        while f:
            phone_number=input('Enter member phone number :')
            if valid.phone_number_validation(phone_number):     #validation for mobile number using valid module
                for i,j in self.member_dict.items():
                    if phone_number not in j:
                        f=2
                    else:
                        f=3
                if f==2:
                    member_details.append(phone_number)
                    f=0
                elif f==3:
                    print('phone number is already given. please give alernate number')
        f=1
        while f:
            email=input('Enter member email address :')
            if valid.email_validation(email):
                for i,j in self.member_dict.items():
                    if email not in j:
                        f=2
                    else:
                        f=3
                if f==2:
                    member_details.append(email)
                    f=0
                elif f==3:
                    print('email address is already given. please give alternate email address')
        while True:
            date_format='%d-%m-%Y'
            try:
                _date=input('Enter your date of birth :')
                dob = datetime.datetime.strptime(_date, date_format).date()#converting string date input into date object
                break
            except ValueError:
                print('Incorrect date format.date format is yyyy-mm-dd')
        dob = datetime.datetime.strptime(_date, date_format).date()#converting string date input into date object
        member_details.append(email)
        member_details.append(dob)
        rand_id=(random.sample(phone_number,3))
        mem_id=''
        mem_id=mem_id.join(rand_id)
        member_details.append(mem_id)
        print('Member ID is ',mem_id)        
        self.member_dict[mem_id]=member_details     #storing all details which stored in list into dictionary with the key of member id
        age=datetime.datetime.today().year-dob.year #extracting the year for age
        print('Member added successfully')
        print(f'\nName :{self.member_dict[mem_id][0]}\nAddress :{self.member_dict[mem_id][1]}\
                \nPhone Number :{self.member_dict[mem_id][2]}\nEmail Address :{self.member_dict[mem_id][3]}\nAge :{age}\nMember ID :{self.member_dict[mem_id][6]}')
    def update_member(self):
        if not len(self.member_dict)==0:        #checking the dictionary if anyone has registered
            while True:
                f=0
                u_mem_id=input('Enter member id to update :')
                if u_mem_id in self.member_dict:
                    print('list of member details\n'+'='*20,'\n1.Member name \n2.Member Address \n3.Member phone number\n4.Member email')
                    print('what do you want to update?')
                    ch=input('pick a choice :')
                    if ch=='1':
                        while True:
                            name=input('Enter new name :')     #updating member name into 0th position of given member id value by slicing the list of value
                            if valid.name_validation(name):
                                break
                        self.member_dict[u_mem_id][0]=name
                        break
                    elif ch=='2':
                        while True:
                            addr=input('Enter new address :')      #updating member address into 1st position of given member id value by slicing the list of value
                            if len(addr)>0:
                                break
                            print('address should not be empty')
                        self.member_dict[u_mem_id][1]=addr
                        break
                    elif ch=='3':
                        f=1
                        while f:
                            num=input('Enter new Phone number :')
                            if valid.phone_number_validation(num):        #validation for mobile number
                                for i,j in self.member_dict.items():
                                    if num not in j:
                                        f=2
                                    else:
                                        f=3
                            if f==2:
                                self.member_dict[u_mem_id][2]=num
                                f=0
                            elif f==3:
                                print('phone number is already given. please give alernate number')
                        break
                    elif ch=='4':
                        f=1
                        while f:
                            email=input('Enter new Email address :')
                            if valid.email_validation(email):       #validation for email
                                for i,j in self.member_dict.items():
                                    if email not in j:
                                        f=2
                                    else:
                                        f=3
                            if f==2:
                                self.member_dict[u_mem_id][3]=email
                                print(self.member_dict)
                                f=0
                            elif f==3:
                                print('email address is already given. please give email address')
                        break
                    else:
                        print('Please enter valid choice')
                    
                else:
                        print('Youre not registered. please enter valid member id')
            print('Member updated successfully')
            print(f'\nName :{self.member_dict[u_mem_id][0]}\nAddress :{self.member_dict[u_mem_id][1]}\
                \nPhone Number :{self.member_dict[u_mem_id][2]}\nEmail Address :{self.member_dict[u_mem_id][3]}\nMember ID :{self.member_dict[u_mem_id][4]}')
        else:
            print('nobody is registered')
    def delete_member(self):
        if not len(self.member_dict)==0:
            d_mem_id=input('Enter member id to delete :')
            if d_mem_id in self.member_dict:
                
                
                print('details of the book to be deleted')  
                print(f'\nName :{self.member_dict[d_mem_id][0]}\nAddress :{self.member_dict[d_mem_id][1]}\
                    \nPhone Number :{self.member_dict[d_mem_id][2]}\nEmail Address :{self.member_dict[d_mem_id][3]}\nMember ID :{self.member_dict[d_mem_id][4]}')
                ch=input('Do you want to delete this member(y/n).').lower()
                if ch=='y':
                    print('why do you want to delete the account?\n')
                    print('1.library malfunction\n2.book malfunction\n3.member expired\n4.others')
                    while True:
                        ch=input('Enter the choice :')
                        if ch=='1' or ch=='2' or ch=='3':
                            del(self.member_dict[d_mem_id])
                            break
                        elif ch=='4':
                            other=input('other reason :')
                            del(self.member_dict[d_mem_id])
                            break
                        else:
                            print('please enter valid choice')
                    print('Given member is deleted successfully')
                elif ch=='n':
                    print('Book is not deleted!')
                else:
                    print('Please enter choice between y and n.')
            else:
                print('youre not registered')
        else:
            print('nobody is registered. please enter valid member id')
    def search_member(self):
        if not len(self.member_dict)==0:
            s_mem_id=input('Enter member id to search :')
            if s_mem_id in self.member_dict:        #searching the member using the member id
                print(f'\nName :{self.member_dict[s_mem_id][0]}\nAddress :{self.member_dict[s_mem_id][1]}\
                        \nPhone Number :{self.member_dict[s_mem_id][2]}\nEmail Address :{self.member_dict[s_mem_id][3]}\nMember ID :{self.member_dict[s_mem_id][4]}')
            else:
                print('youre not registered. please enter valid member id')
        else:
            print('nobody is registered')
