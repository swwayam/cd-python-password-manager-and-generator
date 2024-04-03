from cryptography.fernet import Fernet
import random
import string


def write_key():
    """Generate a new encryption key and write it to a file."""
    # TODO: Generate a new encryption key using Fernet.generate_key()
    # TODO: Open the "key.key" file in write binary mode
    # TODO: Write the generated key to the file

def load_key():
    """Load the encryption key from the "key.key" file."""
    # TODO: Open the "key.key" file in read binary mode
    # TODO: Read the contents of the file
    # TODO: Close the file and return the key

def generate_password(length):
    """Generate a random password of the specified length."""
    # TODO: Create a string of characters including letters, digits, and punctuation
    # TODO: Use random.choice() to select random characters from the string
    # TODO: Join the selected characters into a single string
    # TODO: Return the generated password

# Generate the key file if it doesn't exist
try:
    load_key()
except FileNotFoundError:
    write_key()

key = load_key()
fer = Fernet(key)



def view():
    """View existing passwords."""
    # TODO: Open the "passwords.txt" file in read mode
    # TODO: Iterate over each line in the file
    # TODO: Remove any trailing whitespace from the line
    # TODO: Split the line into account name and encrypted password
    # TODO: Decrypt the encrypted password using fer.decrypt()
    # TODO: Print the account name and decrypted password
    # TODO: Close the file

def add():
    """Add a new password."""
    # TODO: Prompt the user for the account name
    # TODO: Prompt the user to choose between generating a password or entering one manually
    # TODO: If the user chooses to generate a password:
    #     - Prompt for the desired password length
    #     - Call the generate_password() function to generate a random password
    #     - Print the generated password
    # TODO: If the user chooses to enter a password manually, prompt for the password
    # TODO: Open the "passwords.txt" file in append mode
    # TODO: Encrypt the password using fer.encrypt()
    # TODO: Write the account name and encrypted password to the file
    # TODO: Close the file

"""Main program loop."""
while True:
    # TODO: Prompt the user to choose an action (view, add, quit)
    # TODO: If the user chooses "view", call the view() function
    # TODO: If the user chooses "add", call the add() function
    # TODO: If the user chooses "quit", break the loop and exit the program
    # TODO: If the user enters an invalid choice, display an error message and continue the loop