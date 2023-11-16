from tabulate import tabulate
import mysql.connector
import cloth_valid
import re
import maskpass
import random
import datetime
try:
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Abisheik@12',
        database='clothstore'
        )
    cur=mydb.cursor(buffered=True)
    cur.execute('create table if not exists customer_details(\
                c_id int primary key not null,\
                c_name varchar(50) not null ,\
                c_phn_num varchar(10) not null unique,\
                c_email varchar(50) not null unique,\
                c_password varchar(50))')
    cur.execute('create table if not exists cart(\
                    cust_id int,\
                    item_id int,\
                    title varchar(50),\
                    size varchar(5),\
                    price float,\
                    quantity int,\
                    total_price float,\
                    status varchar(50) default "not paid")')
        
except Exception as e:
    print(e)
    cloth_valid.log(e)


class Register:
    global dets
    def register(self):
        while True:
            c_name=input('Enter customer name :')
            if cloth_valid.name_validation(c_name):
                break
        while True:
            c_phone_num=input('Enter customer phone number :')
            if cloth_valid.phone_number_validation(c_phone_num):
                break
        while True:
            c_email=input('Enter customer Email id :')
            if cloth_valid.email_validation(c_email):
                break
        while True:
            c_password=input('Enter customer password :')
            if cloth_valid.password_validation(c_password):
                break
        ran_id= random.sample(c_phone_num,3)
        cus_id=''
        cus_id=cus_id.join(ran_id)
        query=('insert into customer_details(c_id,c_name,c_phn_num,c_email,c_password) values(%s,%s,%s,%s,%s)')
        values=(cus_id,c_name,c_phone_num,c_email,c_password)
        cur.execute(query,values)
        mydb.commit()
        print('customer details stored successfully')
    def login(self):
        cur.execute('select count(c_id) from customer_details')
        if len(cur.fetchall())>0:   #chcking if any customer registered 
            while True:
                try:
                    user_ent=input('Enter Email or phone number to login :')
                    cur.execute('select c_id,c_name,c_phn_num,c_email,c_password from customer_details where c_phn_num=%s or c_email=%s',(user_ent,user_ent))
                    user_det=cur.fetchall() #storing the customer details into  a variable
                    if len(user_det)>0: #checking if the customer is registered or entered the valid customer details
                        pa_word=input('Enter user password :')  #maskpass.askpass(mask='X')
                        if user_det[0][4]==pa_word:     #checking password
                            with open('customer_log.txt','a') as f:     #opening log file and writing log
                                f.write('\n{} logged in at {}'.format(user_det[0][1],datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')))
                            cur.execute(f'select item_id,title,size ,total_price from cart where cust_id={user_det[0][0]}')
                            #global dets
                            dets=cur.fetchall()
                            while True:
                                try:
                                    print('1.Browse clothing items\n2.Add item to cart\n3.view cart\n4.Checkout\n5.Exit')
                                    menu_dict={'1':s1.browse_clothing,'2':s1.addtocart,'3':s1.view_cart,'4':s1.checkout}
                                    ch=input('Enter choice :')
                                    if re.match(r'[12345]{1}',ch):
                                        if ch=='5':
                                            
                                            with open('customer_log.txt','a') as f:     #opening log file and writing log
                                                f.write('\n{} logged out at {}'.format(user_det[0][1],datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')))
                                            break
                                        else:
                                            menu_dict[ch](user_det[0][0],user_det[0][1])    #calling function
                                    else:
                                        raise Exception('Please enter valid choice in numerical')
                                except Exception as e:
                                    print(e)
                                    cloth_valid.log(e)
                            break
                        else:
                            raise Exception('you entered wrong password')
                    else:
                        raise Exception('please enter registered Email or phone number or register before login')
                except Exception as e:
                    print(e)
                    cloth_valid.log(e)
        else:
            print('nobody has registered.please register before login!')
    def browse_clothing(self,cus_id,cus_name):
        cur.execute('select item_id,title,brand,price,category,size from avail_cloth')
        print(tabulate(cur.fetchall(),headers=['Item ID','Title','Brand','Price','Category','Size'],tablefmt='grid'))
        while True:
            desc=input('Do you want to filter (y/n) :').lower()
            if cloth_valid.decision(desc):
                break
        if desc=='y':   #filter options in a dictionary
            menu={'1': 'select item_id,title,brand,price,category,size from avail_cloth where brand=%s',
                  '2':'select item_id,title,brand,price,category,size from avail_cloth order by price',
                  '3':'select item_id,title,brand,price,category,size from avail_cloth order by price desc',
                  '4':'select item_id,title,brand,price,category,size from avail_cloth where category=%s',
                  '5':'select item_id,title,brand,price,category,size from avail_cloth where size=%s'}
            while True:
                print('\n\nBY WHICH FIELD DO YOU LIKE TO FILTER\n\n1.product brand\
                    \n2.price low to high\n3.price high to low \n4.category\n5.size\n6.Exit\n\n')
                ch=input('Enter choice :')
                if re.match(r'[123456]{1}',ch):
                    if ch=='2' or ch=='3':
                        cur.execute(menu[ch])   #executing the query using the dictionary values
                    elif ch=='6':
                        break
                    else:
                        value=input('Enter value to filter :')
                        cur.execute(menu[ch],(value,))
                    print(tabulate(cur.fetchall(),headers=['Item ID','title','brand','price','category','size'],tablefmt='grid'))
    def addtocart(self,cus_id,cus_name):
        
        s1.browse_clothing(cus_id,cus_name)     #calling function to show the available clothsa and filter
        cur.execute('select item_id from avail_cloth')
        av_cloth_list=[i[0] for i in cur.fetchall()]    #fetching all the details and storing into a list
        cur.execute(f'select * from cart where cust_id={cus_id}')   #fetching customer cart values and storing into a list
        sel_item_list=[i[1] for i in cur.fetchall()]
        while True:
            try:
                sel_item=input('which item do you want to purchase :')
                if re.match(r'[0-9]',sel_item):
                    if int(sel_item) in av_cloth_list:
                        if int(sel_item) not in sel_item_list:  #checking if the selected item is already in cart or not
                            cur.execute(f'select item_id,title, size,price from avail_cloth where item_id={sel_item}')
                            val=((cus_id,)+cur.fetchall()[0])   #merging the customer id and cart details into a single tuple
                            cur.execute(f'select stock_quantity  from avail_cloth where item_id={sel_item}')
                            ava_quan=int(cur.fetchall()[0][0])  #fetching stock quantity to compare if the stock the available
                            while True:
                                quan=input('Enter quantity :')
                                if cloth_valid.quantity_valid(quan):
                                    quan=int(quan)
                                    if quan<=ava_quan:
                                        tot_price=quan*val[4]   #calculating total price for the single item
                                        break
                                    else:
                                        print(f'Entered quantity is above the available stock.please enter below {ava_quan}.')
                            query=(f'insert into cart(cust_id,item_id,title,size,price,quantity,total_price) \
                                        values(%s,%s,%s,%s,%s,%s,%s)')     #query for storing the values into the cart table
                            val+=(quan,tot_price)   #adding the total price value into the cart tuple as last element
                            cur.execute(query,val)  #executing the query
                            mydb.commit()
                            cur.execute(f'select item_id,title,size,quantity,total_price from cart where cust_id={cus_id}')
                            dets=cur.fetchall()
                            print('\nITEM ADDED TO CART\n')
                        else:
                            while True:     #func for if the selected item is already in item cart
                                quan=input('Enter quantity :')
                                if cloth_valid.quantity_valid(quan):
                                    break
                            cur.execute(f'select stock_quantity  from avail_cloth where item_id={sel_item}')
                            ava_quan=int(cur.fetchall()[0][0])  #fetching available quantity of the selected product
                            cur.execute(f'select item_id,title, size,price from avail_cloth where item_id={sel_item}')
                            val=((cus_id,)+cur.fetchall()[0])   #merging the cutomer id and roduct details
                            quan=int(quan)
                            if quan<=ava_quan:  #checking whether the stock is available for buy
                                cur.execute(f'update avail_cloth set stock_quantity=stock_quantity-{quan} where item_id={sel_item}')
                                tot_price=quan*val[4]   #caculating the totsl price for the product by multiplying the quantity and unit price
                                cur.execute(f'update cart set total_price=total_price+{tot_price} where item_id={sel_item} and cust_id={cus_id}')
                                mydb.commit()   #just updating the total price alone
                                print('\nITEM ADDED TO CART\n')
                        break
                    else:
                        print('Please enter within available cloths')
                else:
                    raise Exception('Please enter numerical values for item id.')
            except Exception as e:
                print(e)
                cloth_valid.log(e)
    def view_cart(self,cus_id,cus_name):
        cur.execute(f'select item_id,title,size,quantity,total_price from cart where cust_id={cus_id}')
        dets=cur.fetchall()
        if len(dets)>0:
            print(tabulate(dets,headers=['Item ID','TITLE','SIZE','TOTAL PRICE'],tablefmt='grid'))
        else:
            print('there are zero products in cart.please add products to the cart.')
    def checkout(self,cus_id,cus_name):
        cur.execute(f'select item_id,title,size,quantity,total_price from cart where cust_id={cus_id}')
        dets=cur.fetchall()
        if len(dets)>0:
            cur.execute('create table if not exists order_history like cart')
            s1.view_cart(cus_id,cus_name)   #calling function to view cart
            cur.execute(f'select sum(total_price) from cart where cust_id={cus_id}')    #calculating total price of the cart
            print('Total amount to be paid is :',(cur.fetchall()[0][0]))    
            print('\n\nBY WHICH MODE DO YOU WANT TO PAY\n1.credit or debit card\n2.upi app')    #payment mode
            while True:
                try:
                    dcsn=input('Enter choice :')
                    if re.match(r'[12]{1}',dcsn):
                        break
                    else:
                        raise Exception('please enter vslid choice !')
                except Exception as e:
                    print(e)
                    cloth_valid.log(e)
            if dcsn=='1':
                while True:
                    card_num=input('Enter your card number :')
                    if cloth_valid.card_valid(card_num):
                        break
                while True:
                    cvv=input('Enter cvv number :')
                    if cloth_valid.cvv_valid(cvv):
                        break
            if dcsn=='2':
                while True:
                    upi_id=input('Enter upi id :')
                    if cloth_valid.upi_valid:
                        break
            
            cur.execute('insert into order_history select * from cart')     #copying the cart details into the order history for the future reference
            mydb.commit()
            cur.execute(f'update order_history set status= "paid" where cust_id={cus_id}')  #converting the status into paid
            mydb.commit()
            cur.execute(f'delete from cart where cust_id={cus_id}') #deleting the cart details of the particular customer after the successful payment
            mydb.commit()
            cur.execute(f'update avail_cloth as ac join cart on ac.item_id= cart.item_id set ac.stock_quantity=ac.stock_quantity-cart.quantity where cust_id={cus_id}')   #reducing the stock quantity according to the given quantity
            mydb.commit()
            print('\n\nPayment completed successfully\n')
        else:
            print('your cart is empty.please purchase a product before checkout!')
s1=Register()
menu_dict={'1':s1.register,'2':s1.login}    #menu function dictionary
while True:
    try:
        print('1.Register\n2.Login\n3.Exit')
        ch=input('Enter choice :')
        if re.match(r"[123]{1}",ch):
            if ch=='3':
                break
            else:
                menu_dict[ch]() #calling function here
        else:
            raise Exception('please enter valid choice in numerical')
    except Exception as e:
         print(e)
         cloth_valid.log(e)
        
