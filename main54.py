

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            
            return func(*args,**kwargs)
        except ValueError:
            if len(args[0])<2:
                return 'Give me phone'
        except IndexError:
            if not args[0]:
                return 'Give me the name'
        except KeyError:
            if  args[0][0] not in args[1].keys():
                return f'{str(args[0])} not have  a phone'
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    
    contacts[name] = phone
    return "Contact added."
    
    
#@input_error
def change_contact(args, contacts):
    name, phone = args

    if name in contacts.keys():
        contacts[name] = phone
        return "Contact changed."
    else:
        return f'{name} have not phone in contacts'
    
@input_error        
def show_phone(args, contacts):
    name = args[0]
    return f'Phone {name} : {contacts[name]}'


def show_all(contacts):
    if contacts=={}:
        return 'No phones'
    else:
        return contacts
    
    
def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command== 'change':
            
            print(change_contact(args,contacts))
        elif command == 'phone':
            print(show_phone(args,contacts))
           
        elif command == 'all':
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()