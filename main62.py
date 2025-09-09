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
          

     
# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("111")
john_record.add_phone("222")
print(john_record.find_phone("1234567890"))
john_record.edit_phone('222','A44')


john_record.add_phone("5555555555")
john_record.remove_phone("555eee")
#john_record.get_phones('222')
print(john_record)

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
print(jane_record)
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
#john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(found_phone)
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
#book.delete("Jane")