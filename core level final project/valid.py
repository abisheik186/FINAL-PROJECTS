import re
def bookid_valid(a):
  try:
    if not a.isspace():
      if re.search(r'^[a-z]{2}[0-9]{3}$',a):
        return True
      else:
        raise Exception('Wrong format.book id should be in the format of ab123.')
    else:
      raise Exception('book id should not be empty.')
  except Exception as e:
    print(e)
def booktitle_valid(a):
  try:
    if len(a)>0:
      if not a.isspace():
        if re.search(r'\w',a):
          return True
        else:
          raise Exception('Book name should not contain special characters')
      else:        
        raise Exception('Book name should not be space alone')
    else:
        raise Exception('Book name should not be empty')
  except Exception as e:
    print(e)
def book_cost_valid(a):
  try:
    if re.search(r"^[1-9]+|[0-9].[0-9]{1,2}|.[0-9]{1,2}",a):
       if int(a)>0:
          return True
       else:
            raise Exception("cost price should not be negative values")
    else:
         raise Exception("cost should contain only price values and should not be empty")
  except Exception as e:            
      print(e)
def isbn(a):
    if re.search("^[97]{2}[8-9]{1}-[0-9]{1}-[0-9]{5}-[0-9]{3}-[0-9]{1}$",a):
        return True
    else:
        print('please enter valid ISBN number with correct pattern')
def genre_validation(a):
  try:
    if re.search(r'[a-zA-Z-]',a):
      return True
    else:
      raise Exception('genre should not be empty and should not contain special characters')
  except Exception as e:
    print(e)
def no_copies(a):
  try:
    if a.isdigit():
      if int(a)>0:
        return True
      else:
        raise Exception('value should not be less than zero')
    else:
      raise Exception('Available copies are should be only in numbers')
  except Exception as e:
      print(e)
  except ValueError as e1:
      print(e1)
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
            print(e)
def name_validation(a):
    try:
        if len(a)>2 and len(a)<25:
            if re.search(r"\b[a-zA-Z\s.]+\b",a):
                return True
            else:
                raise Exception("name should be in alphabet letters")
        else:
            raise Exception("name should be above three characters and below 25 characters")
    except Exception as e:
        print(e)

def decision(a):
  try:
    if re.search(r"\b[ynYN]",a):
      return True
    else:
      raise Exception("please enter only 'y' and 'n'")
  except Exception as e:
    print(e)

