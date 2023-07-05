from datetime import datetime

from note import Note

class NoteService:
    def __init__(self, repository):
        self.repository = repository

    def list_notes(self):
        notes = self.repository.load_notes()
        if notes:
            for note in notes:
                self.print_note_info(note)
        else:
            print("No notes found.")

    def add_note(self):
        title = input("Enter the note title: ")
        body = input("Enter the note body: ")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes = self.repository.load_notes()
        new_note = Note(
            id=len(notes) + 1,
            title=title,
            body=body,
            created_at=created_at,
            updated_at=created_at
        )
        notes.append(new_note)
        self.repository.save_notes(notes)
        print("Note added successfully.")

    def edit_note(self):
        note_id = int(input("Enter the ID of the note to edit: "))
        notes = self.repository.load_notes()
        note = next((n for n in notes if n.id == note_id), None)
        if note:
            new_title = input("Enter the new title (leave blank to keep the existing title): ")
            new_body = input("Enter the new body (leave blank to keep the existing body): ")
            if new_title:
                note.title = new_title
            if new_body:
                note.body = new_body
            note.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.repository.save_notes(notes)
            print("Note updated successfully.")
        else:
            print("Note not found.")

    def delete_note(self):
        note_id = int(input("Enter the ID of the note to delete: "))
        notes = self.repository.load_notes()
        note = next((n for n in notes if n.id == note_id), None)
        if note:
            notes.remove(note)
            self.repository.save_notes(notes)
            print("Note deleted successfully.")
