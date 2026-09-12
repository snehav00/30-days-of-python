print("==== CONTACT BOOK ====\n")

contacts = []

def menu():
    while True:
        print("""\n1. Add a contact
            2. View contacts
            3. Search contact
            4. Update a contact
            5. Delete a contact
            6. Exit
            """)
        
        try:
            option = int(input("\nChoose an option(1-6): "))
            if 1 <= option <= 6:
                break
            print("Invalid option!")
            
        except ValueError:
            print("Invalid number!")
            
    return option


def get_name():
    while True:
        name = input("Name: ").strip()
        
        if name:
            return name
        
        print("Name cannot be empty!\n")


def get_mobile():
    while True:
        mobile = input("Mobile no.: ").strip()
        
        if mobile.isdigit() and len(mobile) == 10:
            return mobile
        
        print("Invalid mobile number!\n")


def get_email():
    while True:
        email = input("Email: ").strip()
        
        if "@" in email and email.index('@') != 0 and "." in email and email.index('.')-email.index('@') > 1:
            return email
        print("Invalid mail!\n")


def add_contact(contacts):
    name = get_name()
    mobile = get_mobile()
    email = get_email()
    
    details = {
        "name": name,
        "mobile": mobile,
        "email": email
        }
    
    contacts.append(details)

