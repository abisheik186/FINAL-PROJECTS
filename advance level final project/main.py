import cloth_valid
import re
print('\n\nWELCOME TO CLOTH STORE\n\n1.admin page \n2.customer page')
while True:
    try:
        ch=input('Enter your choice :')
        if re.match(r'^[12]{1}$',ch):
            if ch=='1':
                print('\n\nADMIN PAGE\n')
                import clothing_store_admin
            else:
                print('\n\nCUSTOMER PAGE\n')
                import clothing_store_customer
            break
        else:
            raise Exception('please enter available option only')
    except Exception as e:
        cloth_valid.log(e)
        print(e)

