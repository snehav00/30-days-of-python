print("==== CONTACT BOOK ====\n")

contacts = []

while True:
    print("""\n1. Add a contact
          2. View contacts
          3. Search contact
          4. Update a contact
          5. Delete a contact
          6. Exit
          """)
    try:
        option = int(input("\nChoose an option(1-5): "))
        if 1 <= option <= 5:
            break;
        print("Invalid option!")
    except ValueError:
        print("Invalid number!")



    
