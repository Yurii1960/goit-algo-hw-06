from collections import UserDict
from datetime import datetime,date,timedelta

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
        if len(phone)!=10 or not phone.isdigit():
           print(phone)
           raise ValueError('Перевірте телефон')
        self.value=phone
        

class Birthday(Field):
    def __init__(self, birthday):
        try:
            data_birthday=datetime.strptime (birthday, '%d.%m.%Y').date()
            self.value=data_birthday
        except ValueError:
            raise KeyError("Invalid date format. Use DD.MM.YYYY")
 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    

    def add_phone(self,phone):
        self.phones.append(Phone(phone))


    def remove_phone(self,phone):
        p=self.find_phone(phone)
        self.phones.remove(p)
       
    
    def edit_phone(self,old_phone,new_phone):
         p=self.find_phone(old_phone)
         if p==None:
            raise ValueError ('Перевірте номер,який треба замінити ')
         else:
            self.add_phone(new_phone)
            self.remove_phone(p.value)
    
    
    def find_phone(self,phone):
        for p in self.phones:
            if p.value==phone:
                return p
            
    
    

class AddressBook(UserDict):
    def add_record (self,record):
        self.data[record.name.value]=record
        return record
    

    def get_upcoming_birthday(self):
        days=7
        upcoming_birthdays = []
        today = date.today()
        for name in self.data:
            record = self.find(name)
            birthday_this_year = record.birthday.value.replace(year=today.year)
            if birthday_this_year<today:
                birthday_this_year=record.birthday.value.replace(year=today.year+1)
            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday()== 5:
                     birthday_this_year=birthday_this_year+timedelta(days=2)
                elif birthday_this_year.weekday()== 6:
                    birthday_this_year=birthday_this_year+timedelta(days=1)
                congratulation_date_str = birthday_this_year.strftime("%d.%m.%Y")
            upcoming_birthdays.append({"name": name, "congratulation_date": congratulation_date_str})
        return upcoming_birthdays


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
        return '  '.join((f"(Name:{key},phones:{' '.join(p.value for p in self.data[key].phones)},birthday:{self.data[key].birthday})" for key in self.data ))
    

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            if not args[0]:
                return 'Give me the name'
            if  len (args[0])<2:
                return 'Give me phone'
            if len(args[0][1])!=10 or not (args[0][1]).isdigit():
                return 'Check the phone'
            if len(args[0])<3:
                return 'Give me new phone'
            
        except IndexError:
            if not args[0]:
                return 'Give me  name'
            if  len (args[0])<2:
                return 'give me date birthday'
        except KeyError:
            return ("Invalid date format. Use DD.MM.YYYY")
            
        except AttributeError:
                return f'{str(args[0][0])} not have  a record'
    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone,*_= args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message
     
    
@input_error
def change_phone(args,book: AddressBook ):
    name,old_phone,new_phone = args
    if len(args)<3:
        raise IndexError
    record = book.find(name)
    for p in record.phones:
        if p.value == old_phone and new_phone :
            record.phones.remove(p)
            record.add_phone(new_phone)
            return "phone changed."


@input_error        
def show_phone(args,book: AddressBook ):
    name = args[0]
    record = book.find(name)
    return f"(Name:{name},phones:{' '.join(p.value for p in record.phones)})"


def show_all(book: AddressBook ):
    if book=={}:
        return 'No phones'
    else:
        return book

@input_error
def add_birthday(args, book):
    name = args[0]
    birthday = args[1]
    record = book.find(name)
    if birthday:
        record.birthday=Birthday(birthday)
    return "Date birthday added"
    

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    date_birthday=datetime.strftime(record.birthday.value,"%d.%m.%Y")
    return f" Name:{name},Birthday:{date_birthday}"

@input_error
def birthday(args, book):
    return book.get_upcoming_birthday()



def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if  user_input.split()==[]:
            print("Give me the command")
            continue
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args,book))
        elif command== 'change':
            print(change_phone(args,book))
        elif command == 'phone':
            print(show_phone(args,book))
        elif command == 'all':
            print(show_all(book))
        elif command =='add-birthday':
            print(add_birthday(args,book))
        elif command=='show-birthday':
            print(show_birthday(args,book))
        elif command =='birthday':
            print(birthday(args,book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
