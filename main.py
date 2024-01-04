'''project K9'''
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

from classes import (
    Name,
    Phone,
    Email,
    Record,
    AddressBook,
    PhoneError,
    BDayError,
    EmailError,
)
from constants import (
    TITLE,
    FILENAME,
    NOTE_FILENAME,
    HELP_LIST,
    HELP_LIST_ADD,
    HELP_LIST_EDIT,
    HELP_LIST_DEL,
    HELP_LIST_CONTACT,
    HELP_LIST_PHONE,
    HELP_LIST_NOTE,
    HELP_LIST_FIND,
    PROMPT_COMMANDS,
    RED,
    BLUE,
    CYAN,
    GRAY,
    WHITE,
    RESET,
    MAGENTA,
)

from input_output import Console

from notes import NotesBook, NoteError



from sort_path import sorting

book = AddressBook()
notes = NotesBook()


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return f"{RED}not enough params{RESET}\n\tFormat: '<command> <name> <args>'\n\tUse 'help' for information"
        except KeyError:
            return f"{RED}Unknown name {args[0]}. Try another or use help{RESET}"
        except ValueError:
            return f"{RED}time data does not match format 'dd-mm-YYYY' (dd<=31, mm<=12){RESET}"
        except BDayError:
            return f"{RED}time data does not match format 'dd-mm-YYYY' (dd<=31, mm<=12) {RESET}"
        except PhoneError:
            return f"{RED}the phone number must contains only digits, format: '0671234567' or '+380671234567'{RESET}"
        except EmailError as ee:
            return f"{RED} {ee}{RESET}"
        # except AttributeError:
        #    return f"{RED}phone number {args[1]} is not among the contact numbers of {args[0]} {RESET}"
        except AttributeError as ae:
            return f"{RED} {ae}{RESET}"
        except TypeError as ve:
            return f"{RED} {ve}{RESET}"
        except NoteError as ne:
            return f"{RED} {ne}{RESET}"

    return inner


def get_record_or_error(name, book, return_error=False):
    name_rec = Name(name)
    rec = book.get(str(name_rec))
    if not rec:
        error_message = (
            f"{RED}contact {WHITE}{name}{RED} not found in address book{RESET}"
        )
        if return_error:
            return error_message
        else:
            return rec
    return rec


@user_error
def add_birthday(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).add_birthday((args[1]))
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def add_address(*args):
    if get_record_or_error(args[0], book):
        addr_str = ""
        # join args with " " starting from 1
        addr_str = " ".join(args[1:])
        return get_record_or_error(args[0], book).add_address((addr_str))
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def add_email(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).add_email(args[1])
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def add_contact(*args):
    if get_record_or_error(args[0], book):
        return f"{RED}contact {Name(args[0])} already exist{RESET}\n\t{get_record_or_error(args[0], book)}\n\tUse 'add_phone' or 'change' command to add or change the phone"
    book.add_record(Record(args[0]))

    if len(args) > 1:
        if all([args[-1][2] == args[-1][5] == "-", len(args[-1]) == 10]):
            add_birthday(args[0], args[-1])
            args = args[:-1]
        add_phones(args[0], *args[1:])

    return f"contact {Name(args[0])} has been successfully added \n\t{get_record_or_error(args[0],book)}"


@user_error
def add_few_phones(rec, *args):
    result = ""
    for _phone in args:
        rec.add_phone(_phone)
        result += (
            f"phone number {Phone(_phone)} has been added to {rec.name}'s contact list\n"
        )
    return result


@user_error
def add_phones(*args):
    rec = get_record_or_error(args[0], book)
    if rec:
        return add_few_phones(rec, *args[1:]) + f"\t{rec}"
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def change_name(*args):
    return book.change_name((args[0]), args[1])


@user_error
def change_phone(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).edit_phone(
            Phone(args[1]), Phone(args[2])
        )
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def change_email(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).edit_email(
            Email(args[1]), Email(args[2])
        )
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def del_phone(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).remove_phone(Phone(args[1]))
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def del_email(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).remove_email(Email(args[1]))
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def change_address(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).edit_address(args[1])
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def del_address(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).remove_address()
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def delete_record(*args):
    return book.delete_record(args[0])


@user_error
def name_find(*args):
    return book.find_name(args[0])


# =================== Notes begin =========================


@user_error
def add_note(*args):
    if any([not args, len(args) < 2]):
        return f"{RED}not enough params \n\t{WHITE}format: 'add_note <title> <content> {GRAY}<#tags>{WHITE}'{RESET}"
    tags = []
    content_list = []
    for arg in args[1:]:
        if arg.startswith("#"):
            tags.append(arg)
        else:
            content_list.append(arg)
    return notes.add_note(args[0], " ".join(content_list), tags)


@user_error
def add_tag(*args):
    if any([not args, len(args) < 2]):
        return f"{RED}not enough params \n\t{WHITE}format: 'add_note <title> <#tags>'{RESET}"
    title = args[0]
    tags = list(args[1:])
    return notes.add_tags(title, tags)


@user_error
def edit_note(*args):
    if any([not args, len(args) < 2]):
        return f"{RED}not enough params\n\t{WHITE}format: 'edit_note <title> <new_content>'{RESET}"
    return notes.edit_note(args[0], " ".join(args[1:]))


@user_error
def change_tag(*args):
    if any([not args, len(args) < 3]):
        return f"{RED}not enough params\n\t{WHITE}format: 'change_tag <title> <#old_tag> <#new_tag>'{RESET}"
    return notes.change_tags(args[0], args[1], args[2])


@user_error
def delete_note(*args):
    if not args:
        return f"{RED}title is required{RESET}\n\t{WHITE}format: 'delete_note <title>'{RESET}"
    return notes.delete_note(args[0])


@user_error
def delete_tag(*args):
    if any([not args, len(args) < 2]):
        return f"{RED}not enough params\n\t{WHITE}format: 'delete_tag <title> <#tag>'{RESET}"
    return notes.delete_tags(args[0], args[1])


@user_error
def search_notes(*args):
    if not args:
        return f"{RED}searching string is required{RESET}\n\t{WHITE}format: 'search_notes <search_string>'{RESET}"
    return notes.search_notes(args[0])


# =================== Notes end =========================


@user_error
def search(*args):
    result = ""
    if not args:
        return f"{RED}searching string is required{RESET}"
    seek = args[0].lower()
    for record in book.data.values():
        if seek.isdigit():
            if record.seek_phone(seek):
                result += f"\t{BLUE}[   Phone match] {RESET}{record}\n"
            if record.birthday:
                date_str = record.birthday.value.strftime("%d-%m-%Y")
                if date_str.find(seek) != -1:
                    result += f"\t{MAGENTA}[Birthday match] {RESET}{record}\n"

        if seek in record.name.value.lower():
            result += f"\t{CYAN}[ Name match] {RESET}{record}\n"
        if record.seek_email(seek):
            result += f"\t{BLUE}[Email match] {RESET}{record}\n"
        if record.address:
            addr_str = record.address.value.lower()
            if addr_str.find(seek) != -1:
                result += f"\t{GRAY}[ Address match] {RESET}{record}\n"

    if result:
        return f"data found for your request '{seek}': \n{result[:-1]}"
    else:
        return f"{RED}nothing was found for your request '{seek}'{RESET}"


@user_error
def show_all(*args):
    pages = int(args[0]) if args else len(book.data)
    Console.output("  === Address book ===")
    # print(f"  === Address book ===")
    count = 0
    for _ in book.iterator(pages):
        for item in _:
            Console.output(item)
            # print(item)
            count += 1
        if count < len(book):
            Console.input("  Press Enter for next page: ")
            # input(f"  Press Enter for next page: ")
    return "  --- End of List ---"


@user_error
def show_notes(*args):
    pages = int(args[0]) if args else len(notes.data)
    Console.output("  === Notes ===")
    # print(f"  === Notes ===")
    count = 0
    for _ in notes.iterator(pages):
        for item in _:
            Console.output(item)
            # print(item)
            count += 1
        if count < len(notes):
            Console.input("  Press Enter for next page: ")
            # input(f"  Press Enter for next page: ")
    return "  --- End of List ---"


def help_part(*args):
    help_list = []
    for i in args[0]:
        help_list.append(HELP_LIST[i])
    return "\n".join(help_list)


# ===== helps =====
def help_page(*_):
    return help_part(range(len(HELP_LIST)))


def add(*_):
    return help_part(HELP_LIST_ADD)


def change(*_):
    return help_part(HELP_LIST_EDIT)


def delete(*_):
    return help_part(HELP_LIST_DEL)


def contact(*_):
    return help_part(HELP_LIST_CONTACT)


def phone(*_):
    return help_part(HELP_LIST_PHONE)


def note(*_):
    return help_part(HELP_LIST_NOTE)


def find(*_):
    return help_part(HELP_LIST_FIND)


# ===== helps =====


def say_hello(*_):
    return (
        BLUE + TITLE + RESET + "\t\tType 'help' for information\n   How can I help you?"
    )


def say_good_bay(*_):
    book.write_contacts_to_file(FILENAME)
    notes.write_notes_to_file(NOTE_FILENAME)
    exit("Good bye!")


def unknown(*_):
    return f"{RED}Unknown command. Try again{RESET}"


def birthday(days=0):
    list_birthday = []
    result = f'  === Contacts whose birthday is {"in the next "+str(days)+" days" if days else "today"} ===\n'
    for item in book:
        rec = get_record_or_error(item, book)
        if rec.birthday:
            if int(rec.days_to_birthday(rec.birthday)[0]) <= int(days):
                list_birthday.append(rec)
    if len(list_birthday) == 0:
        return f'{RED}there are no contacts whose birthday is {"in the next "+str(days)+" days" if days else "today"}{RESET}'

    for rec in list_birthday:
        result += str(rec) + "\n"
    result += "  --- End of List --- "
    return result


# =============================================
#                main
# =============================================


COMMANDS = {
    add: ("add", "help_add"),
    add_contact: ("add_record", "add_contact"),
    add_phones: ("add_phone", "add_phones"),
    add_birthday: ("add_birthday", "add_bd", "change_birthday", "change_bd"),
    add_address: ("add_address", "add_adr", "change_address", "change_adr"),
    add_email: ("add_email", "email_add"),
    add_note: ("add_note", "note_add"),
    add_tag: ("add_tag", "tag_add"),
    change_tag: ("change_tag", "edit_tag"),
    change: ("change", "edit"),
    change_name: ("change_name", "name_change", "edit_name"),
    change_phone: ("change_phone", "phone_change", "edit_phone"),
    change_address: ("change_address", "change_adr", "edit_address", "edit_adr"),
    change_email: ("change_email", "email_change", "edit_email"),
    edit_note: ("change_note", "note_change", "edit_note"),
    delete: ("delete", "del"),
    del_phone: ("del_phone", "delete_phone"),
    delete_record: ("delete_contact", "del_contact", "delete_record", "del_record"),
    del_address: ("delete_address", "delete_adr", "del_adr"),
    delete_tag: ("delete_tag", "del_tag"),
    del_email: ("delete_email", "del_email"),
    delete_note: ("delete_note", "del_note"),
    name_find: ("name", "find_name"),
    birthday: ("birthdays", "birthday", "find_birthdays", "bd"),
    search: ("search", "seek", "find_any"),
    search_notes: ("search_notes", "find_notes"),
    help_page: ("help",),
    say_hello: ("hello", "hi"),
    show_all: ("show_all", "show", "list"),
    show_notes: ("show_notes", "show_note", "list_notes"),
    say_good_bay: ("exit", "good_bay", "bye", "by", "close", "end"),
    contact: ("contact", "help_contact", "help_record"),
    phone: ("phone", "help_phone"),
    note: ("note", "notes", "help_note", "help_notes"),
    find: ("find",),
    sorting: ("sorting", "sort_path"),
}


def parser(text: str):
    for func, cmd_tpl in COMMANDS.items():
        for command in cmd_tpl:
            data = text.strip().lower().split()
            if len(data) < 1:
                break
            if data[0] == command:
                return func, data[1:]
    return unknown, []


def func_completer(CMD):
    prompt_dict = {}

    prompt_command = PROMPT_COMMANDS
    for i in prompt_command:
        prompt_dict.update({i: None})

    # sorted_command = []
    # for i in CMD.values():
    #     for k in i:
    #         sorted_command.append(k)
    # for i in sorted_command:
    #     # print(f"'{i}',")
    #     prompt_dict.update({i: None})

    return prompt_dict


completer = NestedCompleter.from_nested_dict(func_completer(PROMPT_COMMANDS))
# completer = NestedCompleter.from_nested_dict(func_completer(COMMANDS))


def main():
    global book
    global notes
    book = book.read_contacts_from_file(FILENAME)
    notes = notes.read_notes_from_file(NOTE_FILENAME)
    Console.output(say_hello())
    while True:
        # user_input = Console.input(f"{BLUE}>{CYAN}>{YELLOW}>{RESET}")
        user_input = prompt(">>>", completer=completer)
        func, data = parser(user_input.strip().lower())
        Console.output(func(*data))
        if func not in [
            say_good_bay,
            show_all,
            show_notes,
            say_hello,
            help_page,
            search,
            search_notes,
            name_find,
            find,
            birthday,
            add,
            change,
            delete,
            contact,
            phone,
            note,
            sorting,
        ]:
            book.write_contacts_to_file(FILENAME)
            notes.write_notes_to_file(NOTE_FILENAME)


if __name__ == "__main__":
    main()
