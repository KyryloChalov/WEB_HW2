from collections import UserDict
from constants import RED, GRAY, CYAN, MAGENTA, YELLOW, RESET, WHITE, LEN_OF_NAME_FIELD
import os.path
import pickle
from classes import Field
from input_output import Console


class NoteError(Exception):
    ...


class Title(Field):
    ...


class Content(Field):
    def __init__(self, content):
        super().__init__(content)

    def edit_content(self, new_content):
        self.value = new_content

    def lower(self):
        return self.value.lower()


class Tags(Field):
    def __init__(self, tags=None):
        super().__init__(tags)

    def add_tags(self, new_tags):
        if not self.value:
            self.value = ""  # new_tags
        new_list = list(self.value)
        self.value = new_list + new_tags

    def change_tag(self, old_tag, new_tag):
        if not old_tag in self.value:
            return f"Tag {old_tag} not in Tag list"
        old_list_tag = []
        for o_t in self.value:
            old_list_tag.append(o_t)
        old_list_tag[old_list_tag.index(old_tag)] = new_tag
        self.value = old_list_tag

    def delete_tag(self, tag):
        if not tag in self.value:
            return f"Tag {tag} not in Tag list"
        self.value.remove(tag)

    def __iter__(self):
        return iter(self.value)


class Note:
    def __init__(self, title, content, tags=None):
        self.title = Title(title)
        self.content = Content(content)
        self.tags = Tags(tags) if tags else []

    def __str__(self) -> str:
        blanks = " " * (LEN_OF_NAME_FIELD - len(str(self.title)))
        tags_str = ", ".join(self.tags)
        if len(tags_str) > 0:
            if tags_str[0] == ",":
                tags_str = tags_str[2:]
        return f"{GRAY}•{RESET}{blanks}{CYAN}{self.title}{RESET}  {GRAY}: {RESET}{self.content} \t{MAGENTA}{tags_str}{RESET}"


class NotesBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_note(self, title, content, tags=None):
        new_note = Note(title, content, tags if tags else [""])
        self.data[title] = new_note
        return f"Note '{title}' has been successfully added.\n\t{self.data[title]}"

    def edit_note(self, title, new_content):
        if title in self.data:
            self.data[title].content = new_content
            return f"Note '{title}' has been successfully edited.\n\t{self.data[title]}"
        else:
            return f"Note '{title}' not found."

    def delete_note(self, title):
        if title in self.data:
            del self.data[title]
            return f"Note '{title}' deleted."
        else:
            return f"Note '{title}' not found."

    def add_tags(self, title, tags):  # метод для додавання тегів
        if title in self.data:
            self.data[title].tags.add_tags(tags)
            return f"Tags {', '.join(tags)} added to the note with title '{title}'.\n\t{self.data[title]}"
        else:
            raise NoteError(f"Note with title '{title}' not found.")

    def change_tags(self, title, old_tag, new_tag):
        if title in self.data:
            self.data[title].tags.change_tag(old_tag, new_tag)
            return f"Tag {old_tag} has been successfully changed to {new_tag} for title '{title}'.\n\t{self.data[title]}"
        else:
            raise NoteError(f"Note with title '{title}' not found.")

    def delete_tags(self, title, tag):
        if title in self.data:
            self.data[title].tags.delete_tag(tag)
            return f"Tag {tag} has been successfully deleted for title '{title}'.\n\t{self.data[title]}"
        else:
            raise NoteError(f"Note with title '{title}' not found.")

    def search_notes(self, search_word):
        matching_notes = []
        for title, note in self.data.items():
            if any(
                [
                    search_word.lower() in title.lower(),
                    search_word.lower() in note.content.lower(),
                    search_word.lower() in " ".join(self.data[title].tags).lower(),
                ]
            ):
                matching_notes.append(f"\t{self.data[title]}")
        if matching_notes:
            sorted_notes = sorted(matching_notes)
            # return f"data found for your request '{search_word}': \n, {'\n'.join(sorted_notes)}"
            # return f"data found for your request '{search_word}': " + "\n, " + repr('\n'.join(sorted_notes))
            return f"data found for your request '{search_word}': \n, {chr(10).join(sorted_notes)}"
        else:
            return f"{RED}nothing was found for your request '{WHITE}{search_word}{RED}'{RESET}"

    def read_notes_from_file(self, fn):
        if os.path.exists(fn):
            with open(fn, "rb") as fh:
                self = pickle.load(fh)
            self.data = dict(sorted(self.items()))
        Console.output(f"{GRAY}the notes has been successfully restored{RESET}")
        return self

    def write_notes_to_file(self, fn):
        with open(fn, "wb") as fh:
            pickle.dump(self, fh)
        return f"{GRAY}the notes has been saved successfully{RESET}"

    def iterator(self, n=None):
        counter = 0
        while counter < len(self):
            yield list(self.values())[counter : counter + n]
            counter += n
