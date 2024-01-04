TITLE = f"\t\t\tPersonal Assistant\t\033[33mteam K-9 project"
FILENAME = "addressbook.bin"
NOTE_FILENAME = "notes.bin"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GRAY = "\033[90m"
RESET = "\033[0m"

LEN_OF_NAME_FIELD = 12  # довжина поля для виводу імені

HELP_LIST = [
    # 0
    f"\t{YELLOW}add_contact {CYAN}<name> <phone>{GRAY}*n {CYAN}<birthday>  {RESET} - add a new contact with a phone number(s) and birthday(optional)\n\t\t\t\t\t\t\t{GRAY}(you can enter several phone numbers for a contact){RESET}",
    f"\t{YELLOW}add_phone {CYAN}<name> <new_phone>{GRAY}*n           {RESET} - add the new phone number for an existing contact\n\t\t\t\t\t\t\t{GRAY}(you can enter several phone numbers for a contact){RESET}",
    f'\t{YELLOW}add_bd {CYAN}<name> <birthday>                 {RESET} - add the birthday data ("dd-mm-yyyy") for an existing contact',
    f"\t{YELLOW}add_address {CYAN}<name> <address>             {RESET} - add the address for an existing contact",
    f"\t{YELLOW}add_email {CYAN}<name> <e-mail>                {RESET} - add the e-mail for an existing contact",
    f"\t{YELLOW}add_note {CYAN}<title> <content> <#tag>        {RESET} - add the new note. The title cannot contain spaces.\n\t\t\t\t\t\t\t{GRAY}(if you need several words in the title, use `_` or `-` between)",
    f"\t{YELLOW}add_tag {CYAN}<title> <#tag>                   {RESET} - add the #tag for an existing note",
    # 7
    f"\t{YELLOW}change_name {CYAN}<name> <new_name>            {RESET} - change the name for an existing contact",
    f"\t{YELLOW}change_phone {CYAN}<name> <phone> <new_phone>  {RESET} - change the phone number for an existing contact",
    f"\t{YELLOW}change_bd {CYAN}<name> <new_birthday>          {RESET} - change the birthday data for an existing contact",
    f"\t{YELLOW}change_address {CYAN}<name> <new_address>      {RESET} - change the phone number for an existing contact",
    f"\t{YELLOW}change_email {CYAN}<name> <email> <new_email>  {RESET} - change the phone number for an existing contact",
    f"\t{YELLOW}change_note {CYAN}<title> <new_content>        {RESET} - change the existing note",
    f"\t{YELLOW}change_tag {CYAN}<title> <#tag> <#new_tag>     {RESET} - change #tag in existing note",
    # 14
    f"\t{YELLOW}delete_contact {CYAN}<name>                    {RESET} - remove an existing contact",
    f"\t{YELLOW}delete_phone {CYAN}<name> <phone>              {RESET} - delete one phone number from an existing contact",
    f"\t{YELLOW}delete_address {CYAN}<name>                    {RESET} - delete address from an existing contact",
    f"\t{YELLOW}delete_email {CYAN}<name> <email>              {RESET} - delete one e-mail from an existing contact",
    f"\t{YELLOW}delete_note {CYAN}<title>                      {RESET} - delete an existing note",
    f"\t{YELLOW}delete_tag {CYAN}<title> <#tag>                {RESET} - delete one #tag from an existing note",
    # 20
    f"\t{YELLOW}search {CYAN}<anything>                        {RESET} - search for any string in the contact data",
    f"\t{YELLOW}name {CYAN}<name>                              {RESET} - search record by the name",
    f"\t{YELLOW}birthdays {CYAN}<days>                         {RESET} - a list of contacts who have a birthday within {GRAY}<days>{RESET} days",
    f"\t{YELLOW}list {GRAY}<pages>                             {RESET} - show all contacts, {GRAY}<pages>(optional) - lines per page{RESET}",
    f"\t{YELLOW}search_notes {CYAN}<anything>                  {RESET} - search for any string in the notes",
    f"\t{YELLOW}list_notes {GRAY}<pages>                       {RESET} - show all notes, {GRAY}<pages>(optional) - lines per page{RESET}",
    f"\t{YELLOW}sort_path {CYAN}<path>                         {RESET} - sort files by in the folders",
    # 27
    f"\t{YELLOW}exit                                     {RESET} - exit from PhoneBook",
    f"\t{YELLOW}help                                     {RESET} - this help-page",
    # 28^
]

HELP_LIST_ADD = [0, 1, 2, 3, 4, 5, 6]
HELP_LIST_EDIT = [7, 8, 9, 10, 11, 12, 13]
HELP_LIST_DEL = [14, 15, 16, 17, 18, 19]
HELP_LIST_CONTACT = [0, 7, 14]
HELP_LIST_PHONE = [1, 8, 15]
HELP_LIST_NOTE = [5, 6, 12, 13, 18, 19, 24, 25]
HELP_LIST_FIND = [20, 21, 23, 24, 25]

PROMPT_COMMANDS = [
    # 'add_record',
    "add_contact",
    "add_phone",
    # "add_phones",
    "add_birthday",
    "add_address",
    "add_email",
    "add_note",
    "add_tag",
    "change_birthday",
    "change_address",
    "change_name",
    # "change_address",
    "change_phone",
    "change_email",
    "change_note",
    "change_tag",
    "edit_birthday",
    "edit_address",
    "edit_name",
    "edit_phone",
    "edit_email",
    "edit_note",
    "edit_tag",
    "delete_contact",
    "delete_phone",
    # "delete_record",
    "delete_address",
    "delete_email",
    "delete_note",
    "delete_tag",
    "find_name",
    "birthdays",
    "search",
    "find_any",
    "help",
    "show",
    "list",
    "show_notes",
    "list_notes",
    "search_notes",
    "exit",
    "close",
    "sort_path",
]
