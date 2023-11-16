import re
import logging
logging.basicConfig(filename='clothstore_error_log.txt',level=logging.DEBUG,format='%(asctime)s - %(message)s')
def log(a):
    logging.debug(str(a))
def title_valid(a):
    try:
       if len(a)>=2:
            if re.match(r"^[a-zA-Z\s]+$",a):
                return True
            else:                    
                raise Exception("Name should contain only alphabets")
       else:                
            raise Exception("Name should not empty or below two characters")
    except Exception as e:
        log(e)
        print(e)
def prod_price_valid(a):
  try:
    if re.search(r"^[1-9]+|[0-9].[0-9]{1,2}|.[0-9]{1,2}",a):
       if float(a)>0:
          return True
       else:
            raise Exception("cost price should not be negative values")
    else:
         raise Exception("cost should contain only price values and should not be empty")
  except Exception as e:
      log(e)
      print(e)
def quantity_valid(a):
  try:
    if int(a)>0:
      return True
    else:
      raise Exception("please enter value above zero")
  except ValueError:
    print('please enter numerical values')
  except TypeError:
    print('please Enter valid numerical values')
  except Exception as e:
      log(e)
      print(e)
def name_validation(a):
    try:
        if len(a)>2 and len(a)<25:
            if re.search(r"\b[a-zA-Z\s.]+\b",a):
                return True
            else:
                raise Exception("name should be in alphabet letters and between ")
        else:
            raise Exception("name should be above three characters and below 25 characters")
    except Exception as e:
      log(e)
      print(e)
def phone_number_validation(a):
    try:
        if re.match(r"\b[0-9]{10}$",a):                
            if re.match(r"\b^[6-9]{1}",a):       #validation for employee phone number
                return True
            else:
                raise Exception("mobile number should starts with either 9 or 8 or 7 or 6")
        else:
            raise Exception("mobile number should be 10 digit long")
           # raise Exception("mobile number should starts with either 9 or 8 or 7 or 6")
    except Exception as e:
      log(e)
      print(e)
def email_validation(a):
  try:
    if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', a):
        if len(a)>10 and len(a)<35:            
          return True
        else:
            raise Exception("Email length should be between ten")
    else:
      raise Exception("Email is not valid.Please enter valid Email")
  except Exception as e:
      log(e)
      rint(e)
    
def password_validation(a):
  try:
    if re.match(r"^[\W]{1}+[a-zA-Z0-9\W]{3,9}$",a):        
      return True
    else:
      raise Exception("pasword should contain minimum three characters and maximum nine characters with combination of letters and numbers and special characters")
  except Exception as e:
    log(e)
    print(e)
def decision(a):
  try:
    if re.search(r"\b[ynYN]",a):
      return True
    else:
      raise Exception("please enter only 'y' or 'n'")
  except Exception as e:
      log(e)
      print(e)
def card_valid(a):
    l='4','5','6'
    try:
        if len(a) in [13,16]:
            if a.startswith(l):
                if re.match(r'^[0-9]+$',a):
                    return True
                else:
                    raise Exception('card number should contain only numbers')
            else:
                raise Exception('card numner should starts with 4 or 5 or 6')
        else:
            raise Exception('card number length should be 13 or 16')
    except Exception as e:
        print(e)
        log(e)
def cvv_valid(a):
    try:
        if re.match(r'^[0-9]{3,4}$',a):
            return True
        else:
            raise Exception('Entered cvv is not valid')
    except Exception as e:
        print(e)
        log(e)
def upi_valid(a):
    try:
        if re.search(r'^[a-zA-Z0-9.-]{2, 256}@[a-zA-Z][a-zA-Z]{2, 64}$',a):
            return True
        else:
            raise Exception('please enter valid upi id')
    except Exception as e:
        print(e)
        log(e)
