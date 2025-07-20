from pprint import pprint   
import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        return json.load(f)


path_of_file = os.path.join(os.path.dirname(__file__), "contacts.json") # Use relative path for cross-platform compatibility
config = load_config()
password = config["Password"]

def load_contact():
    '''Loading contact list from JSON file'''

    try:
        with open(path_of_file, "r") as f:
            return json.load(f)
    
    except FileNotFoundError:
        return [] # Return empty list if file does not exist
    
    except json.JSONDecodeError:
        return [] # Return empty list if file is empty or corrupted


def save_contacts(contacts):
    '''Saving contacts in JSON file'''

    with open(path_of_file,"w") as f:
        json.dump(contacts,f,indent=4)





#Adding a contact
def adding_cont():
    '''Adding new contact(s) to the contact book'''

    contact_list = load_contact()

    try:
        number_of_con = int(input("Enter how many contacts you want to add :- "))
    
    except ValueError:
        print("Invalid Number!!")


    for _ in range(number_of_con):
        duplicate = False

        name = input("Enter Name :- ")

        try:
            phone_no = int(input("Enter Phone Number :- "))
        
        except ValueError:
            print("Invalid Phone Number!!")
            return


        email = input("Enter Email :- ")


        details = {
            "Name":name,

            "Phone Number":phone_no,

            "Email":email
        }

        for contact in contact_list:
            if contact["Name"].lower()==name.lower() or contact["Phone Number"]==phone_no:
                print("Name/Phone Number already exist!!")
                duplicate = True
                break
        
        if not duplicate:
            contact_list.append(details)

    save_contacts(contact_list)
    print("Contact(s) Added Successfully!!")


#To show entire contact list
def showing_cont():
    '''Display all saved contacts'''


    contacts = load_contact()

    if contacts:

        print("\nAll Contacts:-")

        pprint(contacts)
    
    else:

        print("No Contacts Saved Yet!!")


#Search for a contact
def search_cont():
    '''Search for a contact by name'''
    contacts = load_contact()

    name_query = input("Enter the name you want to search :- ").strip().lower()
    found = False

    for contact in contacts:

        if name_query in contact["Name"].lower():

            pprint(contact)

            found = True

            break
    
    if not found:

        print("No Such Contacts!!")


#For deleting a contact
def delete_contact():
    """Delete a contact by name."""
        
    contacts = load_contact()
    name_to_delete = input("Enter name to delete: ").strip().lower()

    updated_list = [c for c in contacts if name_to_delete not in c["Name"].lower()]

    if len(contacts) == len(updated_list):
        print("No such contact to delete.")

    else:
        save_contacts(updated_list)

        print("Contact deleted successfully!")





#For Updating Existing Contact
def update_cont():
    '''Updating an existing contact'''
    contacts = load_contact()
    name_to_update = input("Enter name you want to update :- ").strip().lower()
    updated_cont = False

    for contact in contacts:

        if name_to_update in contact["Name"].lower():

            contact["Name"] = input("Enter updated name :- ").strip()
            try:
                contact["Phone Number"] = int(input("Enter updated phone number :- "))

            except ValueError:
                print("Invaid Number!! Skipping Update")
                return  

            contact["Email"] = input("Enter updated email :- ")

            updated_cont = True
            break
        
    if updated_cont:

        save_contacts(contacts)
        print("Contact Updated Successfully!!")
    
    else:

        print("No such contact!!")

#Main Menu
def menu():
    """Main menu loop."""
    asking_pass = input("Enter Password :- ")
    if asking_pass == password:

        while True:
            print("\n📱 Contact Book Menu:")
            print("1. Add Contact(s)")
            print("2. Show All Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Update Contact")
            print("6. Exit")

            choice = input("Enter your choice (1–6): ").strip()

            if choice == "1":
                adding_cont()
            elif choice == "2":
                showing_cont()
            elif choice == "3":
                search_cont()
            elif choice == "4":
                delete_contact()
            elif choice == "5":
                update_cont()
            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    else:
        print("Password Is Wrong!!")

#For clearing entire contact list once
def clear_data():
    '''Deletind Entire Contact list'''

    confirmation = input("Are you sure, you want to clear your contact list? YES or NO :- ").lower()
    if confirmation == "yes":
        save_contacts([])
        print("All Contacts Deleted Successfully✅")
    else:
        return


    


#Entry Point
if __name__=="__main__":
    menu()
