### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class email:

    # Declare the class variable, with default value, for emails.

    has_been_read = False
 
    # Initialise the instance variables for emails.

    def __init__ (self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.

    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.

email_list = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(x):
    """ x = email_address, y = subject_line, z = email_content """
    email_list.append(x)
    
    # Create 3 sample emails and add it to the Inbox list.
for x in range (1,4):
    new_email = email(f"{x}@mail.com",f"Subject line {x}",f"This is the content for email {x}")
    populate_inbox (new_email)


def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for x in range (len(email_list)):
        print (f"{x} {email_list[x].subject_line}")
     
def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print (f"From: {email_list[choice].email_address}")
    print (f"Subject: {email_list[choice].subject_line}")
    print (f"Content: {email_list[choice].email_content}")
    email_list[choice].mark_as_read()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        choice = int (input ("Select an email to read: "))
        read_email(choice)
        
    elif user_choice == 2:
        # add logic here to view unread emails
        for x in range (len(email_list)):
            if email_list[x].has_been_read==False:
                print (email_list[x].subject_line)
            
    elif user_choice == 3:
        # add logic here to quit appplication
        break

    else:
        print("Oops - incorrect input.")

