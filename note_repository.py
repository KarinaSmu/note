import json

from note_serializer import NoteSerializer

class NoteRepository:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_notes(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                notes = [NoteSerializer.deserialize(item) for item in data]
        except FileNotFoundError:
            notes = []
        return notes

    def save_notes(self, notes):
        data = [NoteSerializer.serialize(note) for note in notes]
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
