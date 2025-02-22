"""Will Morris, Friday Afternoon"""
def process_user_contacts(user_input):
 
    # Get contact name from input, output contact's phone number
    # contacts = dict(pair.split(',') or pair.split(" ") for pair in user_input.split())
    contacts = {}
    for pair in user_input.split(','):
        parts = pair.split()
        if len(parts) == 2:
            contacts[parts[0]] = parts[1]
    
    contact_name = input("Enter the contact name: ")
    if contact_name in contacts:
        print(contacts[contact_name])
    else:
        print("Contact not found.")

if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)


