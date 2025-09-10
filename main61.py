from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
        
    def __init__(self,phone):
        self.value=phone
        if len(phone)!=10 or not phone.isdigit():
           raise ValueError('Перевірте телефон') 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self,phone):
        self.phones.append(Phone(phone))


    def remove_phone(self,phone):
        p=self.find_phone(phone)
        self.phones.remove(p)
       
    
    def edit_phone(self,old_phone,new_phone):
        self.add_phone(new_phone)
        p=self.find_phone(old_phone)
        self.remove_phone(p.value)
    
    
    def find_phone(self,phone):
        for p in self.phones:
            if p.value==phone:
                return p
            
                           
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record (self,record):
        self.data[record.name.value]=record
        return record


    def find(self,name):
        if name  in self.data:
            return self.data[name]
        else:
             return None 
         

    def delete(self,name):
         if name in self.data.keys():
            return self.data.pop(name)
         else:
            return None
         
    
    def __str__(self):
        return '  '.join((f"(Name:{key},phones:{' '.join(p.value for p in self.data[key].phones)})" for key in self.data ))
