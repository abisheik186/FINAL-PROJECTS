import mysql.connector
import cloth_valid
import datetime
from tabulate import tabulate
import maskpass
try:
    mydb=mysql.connector.connect(       #establishing database connection
        host='localhost',
        user='root',
        password='Abisheik@12',
        )
    cur=mydb.cursor(buffered=True)  #creating cursor object
    cur.execute('create database if not exists clothstore')
    cur.execute('use clothstore')
except Exception as e:
    cloth_valid.log(e)
    print(e)
class admin:
    def __init__(self):
        self.user_id='admin'
        self.p_word='admin12'
    def add_prod(self):

        while True:
            pr_title=input('Enter product title :').lower()
            if cloth_valid.title_valid(pr_title):
                break
        while True:
            pr_brand=input('Enter product brand :').lower()
            if cloth_valid.title_valid(pr_brand):
                break
        while True:
            pr_price=input('Enter product price :')
            if cloth_valid.prod_price_valid(pr_price):
                break
        while True:
            categ=input('Enter product category :').lower()
            if cloth_valid. title_valid(categ):
                break
        sizes=['xxs','xs','s','m','l','xl','xxl']
        while True:
            size=input('Enter product sizes :').lower()
            if size in sizes:
                break
            else:
                print('please enter valid size')
        while True:
            quan=input('Enter product stock quantity :')
            if cloth_valid.quantity_valid(quan):
                break
        query=('insert into avail_cloth(title,brand,price,category,size,stock_quantity) values(%s,%s,%s,%s,%s,%s)')
        val=(pr_title,pr_brand,pr_price,categ,size,quan)
        cur.execute(query,val)      #storing values into databse
        mydb.commit()
        print('\nproduct added successfully !')
    def display(self):
        cur.execute('select * from avail_cloth')
        print(tabulate(cur.fetchall(),headers=['title','Brand','price','category','size','stock quantity'],tablefmt='grid'))
    def update(self):
        cur.execute('select * from avail_cloth')
        cloths=cur.fetchall()
        b=False
        while True:
            try:
                u_id=input('Enter product id :')
                for i in cloths:
                    if int(u_id) in i:
                        u_id=int(u_id)
                        b=True
                        break
                if b:
                    break
                else:
                    raise Exception('Entered product id is not valid')
            except Exception as e:
                print(e)
                cloth_valid.log(e)
            except ValueError as e1:
                raise ValueError('please enter valid item id')
                cloth_valid.log(e1)
        cur.execute(f'select * from avail_cloth where item_id ={u_id}')
        lis_col=['title','brand','price','category','size','stock_quantity']
        print('1.product title\n2.product brand\n3.price\n4.category\n5.size\n6.stock quantity')
        while True:
            try:
                ch=int(input('which field do you want to update :'))
                if ch<(len(lis_col)+1):
                    break
                else:
                    raise Exception('please enter valid choice')
            except Exception as e:
                print(e)
                cloth_valid.log(e)                  
        if ch==1:                                   #storing validation function into valid variable for every inputs
            valid=cloth_valid.title_valid
        elif ch==2:
            valid=cloth_valid.title_valid
        elif ch==3:
            valid=cloth_valid.prod_price_valid
        elif ch==4:
            valid=cloth_valid.title_valid
        elif ch==5:
            sizes=['xxs','xs','s','m','l','xl','xxl']
            valid_size= lambda a: True if a in sizes else print('please enter only available size')
            valid=valid_size
        elif ch==6:
            valid=cloth_valid.quantity_valid
        while True:
            value=input(f'Enter new value for {lis_col[ch-1]} :')
            if valid(value):
                break
        query=(f'update avail_cloth set {lis_col[ch-1]}=%s where item_id=%s')
        tup=(value,u_id)
        cur.execute(query,tup)
        mydb.commit()
        print(f'\n{lis_col[ch-1]} updated successfully')
    def remove(self):
        cur.execute('select * from avail_cloth')
        table_val=cur.fetchall()
        b=False
        while True:
            try:
                d_id=int(input('Enter item id to delete :'))
                for i in table_val:
                    if d_id in i:                        
                        b=True
                        break
                if b:
                    break
                else:
                    raise Exception('please enter available item id')
            except Exception as e:
                print(e)
                cloth_valid.log(e)
            except ValueError as e1:
                raise ValueError('please enter valid item id')
                cloth_valid.log(e1)
        cur.execute(f'delete from avail_cloth where item_id={d_id}')
        mydb.commit()
        print('\n item deleted successfully')
    def view_orders(self):
        cur.execute('select * from order_history')
        print(tabulate(cur.fetchall(),headers=['customer ID','product ID','product Title','size','unit price','amount','status'],tablefmt='grid'))
    def main(self):
        cur.execute('create table if not exists avail_cloth\
                    (item_id int primary key auto_increment,\
                    title varchar(50) not null,\
                    brand varchar(50) not null,\
                    price float not null,\
                    category varchar(50) not null,\
                    size varchar(5) not null,\
                    stock_quantity int not null)')
        while True:
            admin_id=input('Enter user id :')
            if admin_id==self.user_id:
                admin_pw=input('Enter user password :')#maskpass.askpass(mask='X')
                if admin_pw==self.p_word:
                    with open('admin_log.txt','a') as f:
                        f.write('\nadmin logged in at {}'.format(datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')))
                    while True:
                        print('\n\nWELCOME TO THE CLOTHING STORE INVENTORY MANAGEMENT SYSTEM')
                        print('\n1.Add clothing item\n2.Retrieve clothing item\n3.Update clothing item\
                            \n4.Remove clothing item\n5.view orders\n6.Exit')
                        menu_dict={'1':s1.add_prod,'2':s1.display,'3':s1.update,'4':s1.remove,'5':s1.view_orders}   #dictionary for every function
                        ch=input('Enter choice :')
                        if ch=='6':
                            break
                        else:
                            if ch in menu_dict:     
                                opt=menu_dict[ch]   #storing dict value into a variable
                                opt()   #calling the stored function
                            else:
                                print('invalid choice')
                    break
                else:
                    print('please enter valid password')
            else:
                print('please enter valid user id')
s1=admin()
s1.main()
