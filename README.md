# Chat Bot

This is a chat bot program that works with contacts and notes. You can use it to store, edit, delete, and search for your contacts and notes. You can also sort files in folders.

## Features

- Contacts: You can add, change, or delete contact information such as name, phone number, birthday, address, and email. You can also search for contacts by name or any string, and see a list of contacts who have a birthday within a certain number of days.
- Notes: You can add, change, or delete notes with a title, content, and tags. You can also search for notes by title or any string, and see a list of all notes.
- Sorting files: You can sort files in folders by their extensions, names, or sizes.

## Installation


### Install package

You can install this program as a Python package via pip. You can install the package from different sources:

- From the whl file (in the dist folder):
    - Windows:

    ```
    pip install <package name>.whl 
    ```

    - Mac/Linux:

    ```
    pip3 install <package name>.whl 
    ```

- From the package folder:
    - Windows:

    ```
    pip install -e .
    ```

    - Mac/Linux:

    ```
    pip3 install -e .
    ```


## Usage

After installation, you can run the script with the command:

```
chatbot
```

The script has autocomplete functionality, which means that when you enter a command, you can see suggestions with available options. For example, if you type `add_`, you will see `add_contact`, `add_phone`, `add_bd`, etc.

![autocomplete](https://github.com/KyryloChalov/python_core_team9/assets/20092968/655a38f4-43fa-4d3b-b1fb-5f6d5ca6b5b5)




You can also run the `help` command to see all available commands and their descriptions. Here is a screenshot of the help page:

![help1](https://github.com/KyryloChalov/python_core_team9/assets/20092968/e0644487-7b0a-4a42-9156-93b7d711c523)

Here is a list of commands with some examples:

- `add_contact <name> <phone>*n <birthday>`: Add a new contact with a phone number(s) and birthday(optional). You can enter several phone numbers for a contact. For example:

```
add_contact Alice 1234567890 0987654321 01-01-2000
```

This will add a contact named Alice with two phone numbers and a birthday.

- `add_phone <name> <new_phone>*n`: Add the new phone number(s) for an existing contact. You can enter several phone numbers for a contact. For example:

```
add_phone Alice 1111111111 2222222222
```

This will add two new phone numbers for Alice.

- `add_bd <name> <birthday>`: Add the birthday data ("dd-mm-yyyy") for an existing contact. For example:

```
add_bd Alice 02-02-2002
```

This will change Alice's birthday to 02-02-2002.

- `add_address <name> <address>`: Add the address for an existing contact. For example:

```
add_address Alice 123 Main Street
```

This will add an address for Alice.

- `add_email <name> <e-mail>`: Add the e-mail for an existing contact. For example:

```
add_email Alice alice@example.com
```

This will add an e-mail for Alice.

- `add_note <title> <content> <#tag>`: Add a new note with a title, content, and tag(s). You can enter several tags for a note. The title cannot contain spaces. If you want to use several words in the title, you should use `_` or `-` between words. For example:

```
add_note shopping_list milk, eggs, bread #grocery #todo
```

This will add a note with the title "shopping_list", the content "milk, eggs, bread", and the tags "#grocery" and "#todo".

```
add_note birthday-reminder Alice 01-01-2000 #friend #calendar
```

This will add a note with the title "birthday-reminder", the content "Alice 01-01-2000", and the tags "#friend" and "#calendar".

- `add_tag <title> <#tag>`: Add the #tag for an existing note. You can enter several tags for a note. For example:

```
add_tag Shopping-List #urgent
```

This will add the tag "#urgent" for the note with the title "Shopping-List".

- `change_name <name> <new_name>`: Change the name for an existing contact. For example:

```
change_name Alice Bob
```

This will change the name of the contact from Alice to Bob.

- `change_phone <name> <phone> <new_phone>`: Change the phone number for an existing contact. For example:

```
change_phone Bob 1234567890 3333333333
```

This will change the phone number of Bob from 1234567890 to 3333333333.

- `change_bd <name> <new_birthday>`: Change the birthday data for an existing contact. For example:

```
change_bd Bob 02-02-2002 03-03-2003
```

This will change the birthday of Bob from 02-02-2002 to 03-03-2003.

- `change_address <name> <new_address>`: Change the address for an existing contact. For example:

```
change_address Bob 123 Main Street 456 Park Avenue
```

This will change the address of Bob from 123 Main Street to 456 Park Avenue.

- `change_email <name> <email> <new_email>`: Change the e-mail for an existing contact. For example:

```
change_email Bob bob@example.com bob@gmail.com
```

This will change the e-mail of Bob from bob@example.com to bob@gmail.com.

- `change_note <title> <new_content>`: Change the content of an existing note. For example:

```
change_note Shopping-List cheese, butter, jam
```

This will change the content of the note with the title "Shopping-List" to "cheese, butter, jam".

- `change_tag <title> <tag>`: Delete or change one tag for an existing note. For example:

```
change_tag Shopping-List #urgent
```

This will change the tag "#urgent" for the note with the title "Shopping-List".

- `delete_contact <name>`: Remove an existing contact. For example:

```
delete_contact Bob
```

This will delete the contact named Bob.

- `delete_phone <name> <phone>`: Delete one phone number from an existing contact. For example:

```
delete_phone Alice 0987654321
```

This will delete the phone number 0987654321 from Alice.

- `delete_address <name>`: Delete the address from an existing contact. For example:

```
delete_address Alice
```

This will delete the address from Alice.

- `delete_email <name> <email>`: Delete the e-mail from an existing contact. For example:

```
delete_email Alice alice@example.com
```

This will delete the e-mail alice@example.com from Alice.

- `delete_note <title>`: Delete an existing note. For example:

```
delete_note Shopping-List
```

This will delete the note with the title "Shopping-List".

- `delete_tag <title> <tag>`: Delete one tag from an existing note. For example:

```
delete_tag Shopping-List #grocery
```

This will delete the tag "#grocery" from the note with the title "Shopping-List".

- `search <anything>`: Search for any string (>= 3 characters) in the contact or note data. For example:

```
search Alice
```

This will show all contacts and notes that contain the string "Alice".

- `name <name>`: Search for a contact by the name. For example:

```
name Alice
```

This will show the contact named Alice.

- `birthdays <days>`: Show a list of contacts who have a birthday within <days> days. For example:

```
birthdays 7
```

This will show all contacts who have a birthday within 7 days.

- `list <pages>`: Show all contacts, <pages>(optional) - lines per page. For example:

```
list 10
```

This will show the 10 contacts on each page.

- `list_notes <pages>`: Show all notes, <pages>(optional) - lines per page. For example:

```
list_notes 5
```

This will show the 5 notes on the each page.

- `sort_path <path>`: Sort files in the folders by their extensions. For example:

```
sort_path C:\Users\Documents
```
The script will move the files in the folder to subfolders named after their types. For example, all the `.txt` files will be moved to a subfolder called `Documents`, all the `.jpg` files will be moved to a subfolder called `Images`, and so on.
This can help you organize your files in folders by their types and names. For example, you can use it to group all your images, documents, or audio files into separate subfolders. 

- `exit`: Exit from the chat bot program.
- `help`: Show this help page.

## Save Data

The chat bot program uses two binary files to store the contacts and notes data: `addressbook.bin` and `notes.bin`. The program uses the `book` and `notes` related data to read and write the data from and to the files. The program read and loads data from binary files at the beginning of the chat bot working. The program also write data to the binary files after every command that modifies the data to save the changes to the files. The program uses binary files because they are faster and more efficient than text files.
