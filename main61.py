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
    # реалізація класу
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self,phone):
        if len(phone)!=10:
             return print('Номер повинен бути із 10 цифр')
        else:
            self.phones.append(Phone(phone))


    def remove_phone(self,phone):
        for p in self.phones:
            if p.value==phone:
               self.phones.remove(p)
       
    
    def edit_phone(self,old_phone,new_phone):
        for p in self.phones:
            if p.value==old_phone:
               self.phones.remove(p)
               self.phones.append(Phone(new_phone))
        return self.phones
    
    
    def find_phone(self,phone):
        for p in self.phones:
            if p.value==phone:
                return p
            
                           
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record (self,record):
        self.data[record.name.value]=record.phones


    def find(self,name):
        for key in self.data.keys():
            if key==name :
             return Record(key)
        else:
             return None  

    def delete(self,name):
         if name in self.data.keys():
            return self.data.pop(name)
         else:
            return None
    
    def __str__(self):
        
        return '  '.join((f"(Name:{key},phones:{' '.join(p.value for p in self.data[key])})" for key in self.data ))
          

