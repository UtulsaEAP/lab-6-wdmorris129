"""Will Morris, Friday Afternoon"""
def process_user_contacts(user_input):

    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    contacts = dict(pair.split(',') for pair in user_input.split())
    if contact_name in contacts:
        print(contacts[contact_name])
    else:
        print("Contact not found.")

    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
