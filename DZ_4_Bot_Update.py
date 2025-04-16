menu = """
1)hello - print "How can I help you?
2)add ___ +38______ - add new name and phone
3)change __ +38____ - change number
4)phone ___ - phone ____
5)all - show all numbers
6)close / exit - Good bye!
"""
welcome_banner= r"""
    ____  __                          ____        __ 
   / __ \/ /_  ____  ____  ___       / __ )____  / /_
  / /_/ / __ \/ __ \/ __ \/ _ \     / __  / __ \/ __/
 / ____/ / / / /_/ / / / /  __/    / /_/ / /_/ / /_  
/_/   /_/ /_/\____/_/ /_/\___/____/_____/\____/\__/  
                            /_____/                  
"""
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found"
        except IndexError:
            return 'Enter the argument for the command'

    return inner
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone_number = args
    contacts[name] = phone_number
    return 'Contact added'
@input_error
def change_contact(args, contacts):
    name, new_phone_number = args
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return 'Invalid name'
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if not contacts:
        return 'Not found any contact'
    result =[]
    for name, phone in contacts.items():
        result.append(f'name:  {name} phone: {phone}')
    return result

def main():
    contacts = {}
    print(welcome_banner)
    print()
    print("Welcome to our Bot!")
    print()
    print(menu)
    while True:
        user_input = input('Please enter your command: ')
        command, *args = parse_input(user_input)
        if command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'close' or command == 'exit':
            #print(contacts)
            print("Good Bye!")
            break
        else:
            print(f'Incorrect command, please write command from menu: \n{menu}\n')
            continue
main()
